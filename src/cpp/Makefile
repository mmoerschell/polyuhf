# Compiler and flags
CXX = clang++
CXXFLAGS = -std=c++23 -Wall -Wextra -O3 -I/opt/local/include
LDFLAGS = 

# Target executable
TARGET = driver
SOURCES = driver.cpp
OBJECTS = $(SOURCES:.cpp=.o)

# Default target
all: $(TARGET)

# Link the target
$(TARGET): $(OBJECTS)
	$(CXX) $(OBJECTS) -o $(TARGET) $(LDFLAGS)

# Compile source files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean build files
clean:
	rm -f $(OBJECTS) $(TARGET)

# Run the program
run: $(TARGET)
	./$(TARGET)

# Test with a large number
test: $(TARGET)
	@echo "Testing..."
	./$(TARGET)

.PHONY: all clean run test