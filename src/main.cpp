#include <iostream>
#include <string>
//#include <utility>
#include <tuple>

#include "args.h"
#include "logging.h"
#include "files.h"
#include "init.h"

#define APP_VERSION "0.0.1"
#define APP_HELP "data/help.txt"
#define APP_CONF "data/cppps.conf"

void print_help(const std::string& help_message_path)
{
	File help_file(help_message_path, File::Mode::READ);

	bool file_status = help_file.file_status.status_val();
	std::string status_type = help_file.file_status.status_type();

	if (file_status)
	{
		Logging file_log(help_file.file_status._status);

		if (status_type == "error" || status_type == "warning")
		{
			std::cerr << file_log << '\n';
		}
	}

	for (const auto& line: help_file.read_file())
	{
		std::cout << line << '\n';
	}
}

void print_version()
{
   std::cout << APP_VERSION << '\n';
}

int main(int argc, char **argv)
{
	if (argc == 1)
	{
        print_help(APP_HELP);
		return 0;
	}

	Args args(std::vector<std::string>(argv + 1, argv + argc));

	bool args_status = args.args_status.status_val();

	if (args_status)
	{
		Logging args_log(args.args_status._status);
		std::cout << args_log << '\n';
	}

	if (args.action == "help")
	{
		print_help(APP_HELP);
		return 0;
	}

	if (args.action == "version")
	{
		print_version();
		return 0;
	}

	if (args.action == "none")
	{
		std::cerr << "Couldn't parse the arguments... Exiting now.\n";
		return 1;
	}

	auto& args_map = *args.arguments;
	std::cout << "Arguments:\n";
	for (const auto& [key, value]: args_map)
	{
		std::cout << "key: " << key << "\nvalue: " << value << "\n\n";
	}

	Init init("./data");

	if (init.init_status.status_val())
	{
		Logging init_log(init.init_status._status);
		std::cout << init_log << '\n';

		if (init.init_status.status_type() == "error")
		{
			return 1;
		}
	}

	std::cout << "Config:\n";
	for (const auto& [k, v]: init.return_config())
	{
		std::cout << "k: " << k << ", v: " << v << '\n';
	}

	std::cout << "\nPrefs:\n";
	for (const auto& [k, v]: init.return_prefs())
	{
		std::cout << "k: " << k << ", v: " << v << '\n';
	}

	std::cout << "Done\n";

    return 0;
}
