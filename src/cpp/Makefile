# Compiler and flags
CXX = clang++
CXXFLAGS = -std=c++23 -Wall -Wextra -O3 -isystem /opt/local/include
LDFLAGS = -L/opt/local/lib

# Main target
TARGET = driver
SOURCES = references.cpp driver.cpp
OBJECTS = $(SOURCES:.cpp=.o)

# Test target (using pre-built Boost.Test)
TEST_TARGET = test_runner
TEST_SOURCES = references.cpp test_runner.cpp
TEST_OBJECTS = $(TEST_SOURCES:.cpp=.o)
TEST_LDFLAGS = $(LDFLAGS) -lboost_unit_test_framework-mt
TEST_CXXFLAGS = $(CXXFLAGS) -DBOOST_TEST_DYN_LINK  # For dynamic linking

# Default target
all: $(TARGET)

# Link the main target
$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET) $(LDFLAGS)

# Link the test target
$(TEST_TARGET): $(TEST_OBJECTS)
	$(CXX) $(TEST_OBJECTS) -o $(TEST_TARGET) $(TEST_LDFLAGS)

# Compile source files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Special rule for test objects (with different flags)
test_runner.o: test_runner.cpp
	$(CXX) $(TEST_CXXFLAGS) -c $< -o $@

# Clean build files
clean:
	rm -f $(OBJECTS) $(TEST_OBJECTS) $(TARGET) $(TEST_TARGET)

# Run the main program
run: $(TARGET)
	./$(TARGET)

# Build and run tests
test: $(TEST_TARGET)
	@echo "Running tests..."
	./$(TEST_TARGET)

.PHONY: all clean run test