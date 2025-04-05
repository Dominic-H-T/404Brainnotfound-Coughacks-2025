
#include "tokenizer.h"
#include <fstream>
#include <vector>
#include <sstream>
#include <iostream>
#include <filesystem>
#include <regex>

const string TOS_ORGINAL = "orginal_text";

vector<string> tokenize(const string& text)
{
    fstream inFile(TOS_ORGINAL);
    vector<string> tokens;
    string word;

    if(inFile.fail())
    {
        //handle exeptions
    }  
    // read all of the file into the vector
    while (inFile >> word)
    {
        tokens.push_back(word);
    }

}

vector<string> splitIntoSentences(const string& text)
{
    vector<string> sentences;
    regex sentenceEnd(R"([.?!])");
    sregex_token_iterator iter(text.begin(), text.end(), sentenceEnd, -1);
    sregex_token_iterator end;

    while (iter != end) {
        sentences.push_back(*iter++);
    }

    return sentences;

}

