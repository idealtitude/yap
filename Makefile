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

BIN=$(BINDIR)/$(BINNAME)-$(VERSION)

.PHONY: all release version install clean cleanall

all:$(BIN)

release: CXXFLAGS=-std=c++23 -Wall -O2 -DNDEBUG
release: clean
release: $(BIN)

$(BIN): $(OBJS) $(OBJDIR)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $@ $(LDFLAGS)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp $(OBJDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(OBJDIR):
	mkdir -p $@

$(BINDIR):
	mkdir -p $@

version:
	@echo $(BINNAME) version $(VERSIONNO)

install:
	@echo Not yet implemented

clean:
	$(RM) -r $(OBJDIR)

cleanall: clean
	$(RM) -r $(BINDIR)/*
