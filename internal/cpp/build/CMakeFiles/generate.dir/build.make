# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.18

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/main/SSE/dali/internal/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/main/SSE/dali/internal/cpp/build

# Include any dependencies generated for this target.
include CMakeFiles/generate.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/generate.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/generate.dir/flags.make

CMakeFiles/generate.dir/src/app.cpp.o: CMakeFiles/generate.dir/flags.make
CMakeFiles/generate.dir/src/app.cpp.o: ../src/app.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/main/SSE/dali/internal/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/generate.dir/src/app.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/generate.dir/src/app.cpp.o -c /home/main/SSE/dali/internal/cpp/src/app.cpp

CMakeFiles/generate.dir/src/app.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/generate.dir/src/app.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/main/SSE/dali/internal/cpp/src/app.cpp > CMakeFiles/generate.dir/src/app.cpp.i

CMakeFiles/generate.dir/src/app.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/generate.dir/src/app.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/main/SSE/dali/internal/cpp/src/app.cpp -o CMakeFiles/generate.dir/src/app.cpp.s

CMakeFiles/generate.dir/src/digitalAction.cpp.o: CMakeFiles/generate.dir/flags.make
CMakeFiles/generate.dir/src/digitalAction.cpp.o: ../src/digitalAction.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/main/SSE/dali/internal/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/generate.dir/src/digitalAction.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/generate.dir/src/digitalAction.cpp.o -c /home/main/SSE/dali/internal/cpp/src/digitalAction.cpp

CMakeFiles/generate.dir/src/digitalAction.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/generate.dir/src/digitalAction.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/main/SSE/dali/internal/cpp/src/digitalAction.cpp > CMakeFiles/generate.dir/src/digitalAction.cpp.i

CMakeFiles/generate.dir/src/digitalAction.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/generate.dir/src/digitalAction.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/main/SSE/dali/internal/cpp/src/digitalAction.cpp -o CMakeFiles/generate.dir/src/digitalAction.cpp.s

CMakeFiles/generate.dir/src/digitalCondition.cpp.o: CMakeFiles/generate.dir/flags.make
CMakeFiles/generate.dir/src/digitalCondition.cpp.o: ../src/digitalCondition.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/main/SSE/dali/internal/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/generate.dir/src/digitalCondition.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/generate.dir/src/digitalCondition.cpp.o -c /home/main/SSE/dali/internal/cpp/src/digitalCondition.cpp

CMakeFiles/generate.dir/src/digitalCondition.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/generate.dir/src/digitalCondition.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/main/SSE/dali/internal/cpp/src/digitalCondition.cpp > CMakeFiles/generate.dir/src/digitalCondition.cpp.i

CMakeFiles/generate.dir/src/digitalCondition.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/generate.dir/src/digitalCondition.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/main/SSE/dali/internal/cpp/src/digitalCondition.cpp -o CMakeFiles/generate.dir/src/digitalCondition.cpp.s

CMakeFiles/generate.dir/src/init.cpp.o: CMakeFiles/generate.dir/flags.make
CMakeFiles/generate.dir/src/init.cpp.o: ../src/init.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/main/SSE/dali/internal/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/generate.dir/src/init.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/generate.dir/src/init.cpp.o -c /home/main/SSE/dali/internal/cpp/src/init.cpp

CMakeFiles/generate.dir/src/init.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/generate.dir/src/init.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/main/SSE/dali/internal/cpp/src/init.cpp > CMakeFiles/generate.dir/src/init.cpp.i

CMakeFiles/generate.dir/src/init.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/generate.dir/src/init.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/main/SSE/dali/internal/cpp/src/init.cpp -o CMakeFiles/generate.dir/src/init.cpp.s

CMakeFiles/generate.dir/src/main.cpp.o: CMakeFiles/generate.dir/flags.make
CMakeFiles/generate.dir/src/main.cpp.o: ../src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/main/SSE/dali/internal/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/generate.dir/src/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/generate.dir/src/main.cpp.o -c /home/main/SSE/dali/internal/cpp/src/main.cpp

CMakeFiles/generate.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/generate.dir/src/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/main/SSE/dali/internal/cpp/src/main.cpp > CMakeFiles/generate.dir/src/main.cpp.i

CMakeFiles/generate.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/generate.dir/src/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/main/SSE/dali/internal/cpp/src/main.cpp -o CMakeFiles/generate.dir/src/main.cpp.s

CMakeFiles/generate.dir/src/step.cpp.o: CMakeFiles/generate.dir/flags.make
CMakeFiles/generate.dir/src/step.cpp.o: ../src/step.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/main/SSE/dali/internal/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/generate.dir/src/step.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/generate.dir/src/step.cpp.o -c /home/main/SSE/dali/internal/cpp/src/step.cpp

CMakeFiles/generate.dir/src/step.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/generate.dir/src/step.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/main/SSE/dali/internal/cpp/src/step.cpp > CMakeFiles/generate.dir/src/step.cpp.i

CMakeFiles/generate.dir/src/step.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/generate.dir/src/step.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/main/SSE/dali/internal/cpp/src/step.cpp -o CMakeFiles/generate.dir/src/step.cpp.s

# Object files for target generate
generate_OBJECTS = \
"CMakeFiles/generate.dir/src/app.cpp.o" \
"CMakeFiles/generate.dir/src/digitalAction.cpp.o" \
"CMakeFiles/generate.dir/src/digitalCondition.cpp.o" \
"CMakeFiles/generate.dir/src/init.cpp.o" \
"CMakeFiles/generate.dir/src/main.cpp.o" \
"CMakeFiles/generate.dir/src/step.cpp.o"

# External object files for target generate
generate_EXTERNAL_OBJECTS =

generate: CMakeFiles/generate.dir/src/app.cpp.o
generate: CMakeFiles/generate.dir/src/digitalAction.cpp.o
generate: CMakeFiles/generate.dir/src/digitalCondition.cpp.o
generate: CMakeFiles/generate.dir/src/init.cpp.o
generate: CMakeFiles/generate.dir/src/main.cpp.o
generate: CMakeFiles/generate.dir/src/step.cpp.o
generate: CMakeFiles/generate.dir/build.make
generate: CMakeFiles/generate.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/main/SSE/dali/internal/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable generate"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/generate.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/generate.dir/build: generate

.PHONY : CMakeFiles/generate.dir/build

CMakeFiles/generate.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/generate.dir/cmake_clean.cmake
.PHONY : CMakeFiles/generate.dir/clean

CMakeFiles/generate.dir/depend:
	cd /home/main/SSE/dali/internal/cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/main/SSE/dali/internal/cpp /home/main/SSE/dali/internal/cpp /home/main/SSE/dali/internal/cpp/build /home/main/SSE/dali/internal/cpp/build /home/main/SSE/dali/internal/cpp/build/CMakeFiles/generate.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/generate.dir/depend

