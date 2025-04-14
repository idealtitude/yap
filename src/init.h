#ifndef INIT_H
#define INIT_H

#include <unordered_map>
#include <string>
#include <fstream>
#include <filesystem>
#include <regex>

#include "status.h"
#include "files.h"

namespace fs = std::filesystem;

class Init
{
  public:
	Init() = delete;
	/**
	 * @brief this constructor take a path to the configuration file
	 *
	 * @param confp A string containing the path to the configuration file (std::string)
	 */
	Init(const std::string& confp);
	~Init() = default;

    // Attributes
    Status init_status;

    //Methods
    std::unordered_map<std::string, std::string> return_config() const;
    std::unordered_map<std::string, std::string> return_prefs() const;

  private:
    // Attributes
    std::string config_path;
    std::unordered_map<std::string, std::string> _config;
    std::unordered_map<std::string, std::string> _prefs;

    //Methods
    bool dir_exists(const std::string& dir_path);
    void get_config();
    void parse_prefs();
};

#endif // INIT_H
