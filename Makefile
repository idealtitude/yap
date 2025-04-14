# Basic vars & flags
CXX=clang++
CXXFLAGS=-std=c++23 -O0 -W -Wall -Werror -Wextra -Wshadow -pthread -Wno-sign-compare -Wconversion -Wno-unused-function -Wpedantic -pedantic -pedantic-errors -g
LDFLAGS=

# Directories & other
BINNAME=yap
BINDIR=bin
SRCDIR=src
OBJDIR=build
SRCS=$(wildcard $(SRCDIR)/*.cpp)
OBJS=$(patsubst $(SRCDIR)/%.cpp, $(OBJDIR)/%.o, $(SRCS))
VERSIONNO=$(shell cat ./VERSION)
PREFIX ?= $(HOME)/.local

BIN=$(BINDIR)/$(BINNAME)-$(VERSIONNO)

.PHONY: all release version install uninstall clean cleanall

all:$(BIN)

release: CXXFLAGS=-std=c++23 -Wall -O2 -DNDEBUG
release: clean
release: $(BIN)

$(BIN): $(OBJS) $(OBJDIR)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $@ $(LDFLAGS)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(OBJDIR):
	@mkdir -p $@

$(BINDIR):
	@mkdir -p $@

version:
	@echo $(BINNAME) version $(VERSIONNO)

install:
	@echo "Creating configuration directories..."
	@mkdir -p "$(HOME)/.config/yap"
	@mkdir -p "$(PREFIX)/share/yap"
	@mkdir -p "$(PREFIX)/bin"

	@echo "Installing configuration files..."
	@install -D data/yap.conf "$(HOME)/.config/yap/yap.conf"
	@install -D data/user_preferences.conf "$(PREFIX)/share/yap/user_preferences.conf"
	@install -D data/help.txt "$(PREFIX)/share/yap/help.txt"
	@install -D VERSION "$(PREFIX)/share/yap/version.txt"

	@echo "Installing executable..."
	@install -D bin/yap "$(PREFIX)/bin/yap"
	@chmod +x "$(PREFIX)/bin/yap"

	@echo "Installation complete!"

uninstall:
	@echo "Removing installed files and directories..."
	@rm -rf "$(HOME)/.config/yap"
	@rm -rf "$(PREFIX)/share/yap"
	@rm -rf "$(PREFIX)/bin/yap" # Be more specific about removing the bin directory content
	@echo "Uninstallation complete!"

clean:
	$(RM) -r $(OBJDIR)

cleanall: clean
	$(RM) -r $(BINDIR)/*
