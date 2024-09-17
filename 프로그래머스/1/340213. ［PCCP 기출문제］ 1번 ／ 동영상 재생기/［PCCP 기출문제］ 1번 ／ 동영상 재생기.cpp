#include <string>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

vector<string> split(string str, char del) {
    istringstream iss(str);
    string buffer;
    vector<string> result;
    
    while (getline(iss, buffer, del)) result.push_back(buffer);
    return result;
}

int getTime(string strTime) {
    vector<string> splitTime = split(strTime, ':');
    int time = stoi(splitTime[0]) * 60 + stoi(splitTime[1]);
    return time;
}

string formatTime(int time) {
    int minutes = time / 60;
    int seconds = time % 60;
    
    ostringstream oss;
    oss << setw(2) << setfill('0') << minutes << ":";
    oss << setw(2) << setfill('0') << seconds;
    
    return oss.str();
}

string solution(string video_len, string pos, string op_start, string op_end, vector<string> commands) {

    string answer = "";
    int videoTime = getTime(video_len);
    int posTime = getTime(pos);
    int opStart = getTime(op_start);
    int opEnd = getTime(op_end);
    
    if (posTime >= opStart && posTime <= opEnd) posTime = opEnd;
    
    for (auto & command : commands) {
        if (command == "next") {
            posTime += 10;
            if (posTime > videoTime) posTime = videoTime;
        }
        else if (command == "prev") { 
            posTime -= 10;
            if (posTime < 0) posTime = 0;
        }
        if (posTime >= opStart && posTime <= opEnd) posTime = opEnd;
    }
    
    
    return formatTime(posTime);
}
