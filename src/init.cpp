#include "init.h"

Init::Init(const std::string& confp):
    config_path(confp), _config(), _prefs()
{
    get_config();
}

std::unordered_map<std::string, std::string> Init::return_config() const
{
    return _config;
}

std::unordered_map<std::string, std::string> Init::return_prefs() const
{
    return _prefs;
}

bool Init::dir_exists(const std::string& dir_path)
{
    fs::path _path{std::string(dir_path)};
    fs::directory_entry _dir{_path};

    if (!_dir.exists())
    {
        return false;
    }

    return true;
}

void Init::get_config()
{
    if (!dir_exists(config_path))
    {
        std::string errmsg = "configuration directory has not been found!\nExpected location: " + config_path + "; check the installation or provide another path (see doc/doc.md and/or see the help (with the -h flag) for more information)";
        init_status.set_status(true, "error", errmsg);
        return;
    }

    _config.insert({"help", std::string(config_path).append("/help.txt")});
    _config.insert({"version", std::string(config_path).append("/version.txt")});
    _config.insert({"prefs", std::string(config_path).append("/cppps.conf")});

    parse_prefs();
}

void Init::parse_prefs()
{
	File prefs_file(_config["prefs"], File::Mode::READ);
	std::vector<std::string> prefs_content = prefs_file.read_file();

	if (prefs_file.file_status.status_type() != "error")
	{
        std::regex prefs_ptn{R"(^([a-z0-9_]+)=\"(.*)\"$)"};
        std::smatch _m;

		for (const std::string& line: prefs_content)
		{
			if (line.starts_with("#"))
			{
				// Skipping comments
				continue;
			}
			if (std::regex_search(line, _m, prefs_ptn))
            {
                if (_m.size() < 3) // ignore ill formated lines
                {
					std::string errmsg = "unknown or ill formatted key/value pair: " + line;
					init_status.set_status(true, "warning", errmsg);
                    continue;
                }

                _prefs.insert({std::string(_m[1]), std::string(_m[2])});
            }
		}
	}
	else
	{
		// TODO: use copy constructor?
		init_status.set_status(true, prefs_file.file_status.status_type(), prefs_file.file_status.status_msg());
	}
}
