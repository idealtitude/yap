#include "node.h"

Node::Node(const std::string& tag_name):
	parent(),
	tag(tag_name),
	attributes(),
	text(),
	indent(0),
	autoclose(false),
	children()
{}

void Node::add_child(std::shared_ptr<Node> child)
{
    children.push_back(child);
    child->parent = shared_from_this();
}
