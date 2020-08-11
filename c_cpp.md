# C and C++ notes

#### Check if a file exists

```
#include <sys/stat.h>
#include <unistd.h>
#include <string>
#include <fstream>

// Method exists_test0 (ifstream): **0.485s**
inline bool exists_test0 (const std::string& name) {
    ifstream f(name.c_str());
    return f.good();
}

// Method exists_test1 (FILE fopen): **0.302s**
inline bool exists_test1 (const std::string& name) {
    if (FILE *file = fopen(name.c_str(), "r")) {
        fclose(file);
        return true;
    } else {
        return false;
    }   
}

// Method exists_test2 (posix access()): **0.202s**
// Only on Posix - Linux compiled with g++
inline bool exists_test2 (const std::string& name) {
    return ( access( name.c_str(), F_OK ) != -1 );
}

// Method exists_test3 (posix stat()): **0.134s**
// Only on Posix - Linux compiled with g++
inline bool exists_test3 (const std::string& name) {
  struct stat buffer;   
  return (stat (name.c_str(), &buffer) == 0); 
}
```