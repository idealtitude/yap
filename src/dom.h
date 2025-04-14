#ifndef DOM_H
#define DOM_H

#include <string>
//#include <map>
#include <vector>
#include <memory>

#include "node.h"

class Dom
{
  public:
	Dom();
	~Dom() = default;

	std::shared_ptr<Node> get_root() const { return root; }

  private:
	std::shared_ptr<Node> root;
};

#endif // DOM_H
