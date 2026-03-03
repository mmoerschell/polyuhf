# Compiler
CXX = clang++
CXXFLAGS_BASE = -std=c++26 -Wall -Wextra -Wpedantic -isystem /opt/local/include
LDFLAGS = -L/opt/local/lib -lboost_unit_test_framework-mt

# Release flags
CXXFLAGS_RELEASE = -O3 -DNDEBUG
# Debug flags
CXXFLAGS_DEBUG = -O0 -g -fno-omit-frame-pointer

# Sources
SRC = $(filter-out main.cpp, $(wildcard *.cpp))
TESTS = tests.cpp

# Object directory
BUILD_RELEASE = build/release
BUILD_DEBUG   = build/debug

# Object files
OBJ_RELEASE = $(addprefix $(BUILD_RELEASE)/, $(SRC:.cpp=.o)) $(BUILD_RELEASE)/tests.o
OBJ_DEBUG   = $(addprefix $(BUILD_DEBUG)/, $(SRC:.cpp=.o)) $(BUILD_DEBUG)/tests.o

# Target executables
TARGET_TEST_RELEASE = $(BUILD_RELEASE)/tests
TARGET_TEST_DEBUG   = $(BUILD_DEBUG)/tests

.PHONY: all release debug run-test debug-test clean

all: release debug

# --------------------
# Release test build
# --------------------
release: $(TARGET_TEST_RELEASE)

$(TARGET_TEST_RELEASE): $(OBJ_RELEASE)
	$(CXX) $^ -o $@ $(LDFLAGS)

$(BUILD_RELEASE)/%.o: %.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS_BASE) $(CXXFLAGS_RELEASE) -c $< -o $@

run-test: release
	$(TARGET_TEST_RELEASE)

# --------------------
# Debug test build
# --------------------
debug: $(TARGET_TEST_DEBUG)

$(TARGET_TEST_DEBUG): $(OBJ_DEBUG)
	$(CXX) $^ -o $@ $(LDFLAGS)

$(BUILD_DEBUG)/%.o: %.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS_BASE) $(CXXFLAGS_DEBUG) -c $< -o $@

debug-test: debug
	lldb $(TARGET_TEST_DEBUG)

# --------------------
# Clean
# --------------------
clean:
	rm -rf build
