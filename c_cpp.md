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

### Run command and get output
```
#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>

std::string exec(const char* cmd)
{
    std::array<char, 128> buffer;
    std::string result;
    auto pipe = popen(cmd, "r");
    
    if (!pipe) throw std::runtime_error("popen() failed!");
    
    while (!feof(pipe))
    {
        if (fgets(buffer.data(), 128, pipe) != nullptr)
            result += buffer.data();
    }
    
    auto rc = pclose(pipe);
    
    if (rc == EXIT_SUCCESS)
    {
        std::cout << "SUCCESS\n";
    }
    else
    {
        std::cout << "FAILED\n";
    }
    
    return result;
}

using namespace std;

int main()
{
    cout<<"Start\n";
    std::string res;
    
    res = exec("cp d-oh");
    std::cout << "cp stdout res: <" << res << ">" << std::endl;

    res = exec("cp d-oh 2>&1");
    std::cout << "cp stdout&stderr res: <" << res << ">" << std::endl;

    res = exec("echo stdout 2>&1 >&1");
    std::cout << "stdout res: <" << res << ">" << std::endl;
    
    res = exec("echo stderr 2>&1 >&2");
    std::cout << "stderr res: <" << res << ">" << std::endl;
    

    cout<<"End\n";
    return 0;
}
```

### split string by newline
```
std::vector<std::string> split_string_by_newline(const std::string& str)
{
    auto result = std::vector<std::string>{};
    auto ss = std::stringstream{str};

    for (std::string line; std::getline(ss, line, '\n');)
        result.push_back(line);

    return result;
}
```
