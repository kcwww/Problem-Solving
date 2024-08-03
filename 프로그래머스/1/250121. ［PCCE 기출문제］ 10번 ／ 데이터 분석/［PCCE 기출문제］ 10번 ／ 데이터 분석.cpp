#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

enum VALEXT {
    CODE,
    DATE,
    MAX,
    REMAIN
};

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;
    
    if (ext == "date") {
        for (const auto & value : data) {
            if (value[DATE] <= val_ext) answer.push_back(value);
        }
    } else if (ext == "code") {
        for (const auto & value : data) {
            if (value[CODE] <= val_ext) answer.push_back(value);
        }
    } else if (ext == "maximum") {
        for (const auto & value : data) {
            if (value[MAX] <= val_ext) answer.push_back(value);
        }
    } else {
        for (const auto & value : data) {
            if (value[REMAIN] <= val_ext) answer.push_back(value);
        }
    }
    
    if (sort_by == "date") {
        sort(answer.begin(), answer.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[DATE] < b[DATE];
    });
    } else if (sort_by == "code") {
        sort(answer.begin(), answer.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[CODE] < b[CODE];
    });
        
    } else if (sort_by == "maximum") {
        sort(answer.begin(), answer.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[MAX] < b[MAX];
    }); 
    } else {
        sort(answer.begin(), answer.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[REMAIN] < b[REMAIN];
    });
    }
    
    return answer;
}