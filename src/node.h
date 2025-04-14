#ifndef NODE_H
#define NODE_H

#include <string>
#include <map>
#include <vector>
#include <memory>

struct Node : public std::enable_shared_from_this<Node>
{
  public:
	Node() = delete;
	Node(const std::string& tag_name);
	~Node() = default;

	std::weak_ptr<Node> parent;
	std::string tag;
	std::map<std::string, std::string> attributes;
	std::string text;
	int indent;
	bool autoclose;
	std::vector<std::shared_ptr<Node>> children;

	void add_child(std::shared_ptr<Node> child);
};

#endif // NODE_H
