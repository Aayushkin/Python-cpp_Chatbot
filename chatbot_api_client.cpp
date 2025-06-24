#include <iostream>
#include <string>
#include <curl/curl.h>
#include <sstream>
#include <unistd.h> // for usleep()
#include <regex>

using namespace std;

// Write callback to capture the API response
size_t WriteCallback(void* contents, size_t size, size_t nmemb, string* output) {
    size_t totalSize = size * nmemb;
    output->append((char*)contents, totalSize);
    return totalSize;
}

// Extract reply from JSON like {"reply":"..."}
string extractReply(const string& json) {
    std::smatch match;
    std::regex rgx("\"reply\"\\s*:\\s*\"([^\"]*)\"");
    if (std::regex_search(json, match, rgx) && match.size() > 1) {
        return match[1];
    }
    return "Error: Could not extract reply.";
}

// Simulated typing effect
void typeOut(const string& text, int speed = 25000) {
    for (char ch : text) {
        cout << ch << flush;
        usleep(speed); // microseconds
    }
    cout << endl;
}

// Color helpers
void printUser(const string& text) {
    cout << "\033[1;33mYou: " << text << "\033[0m" << endl; // Yellow
}

void printBot(const string& text) {
    cout << "\033[1;32mAayuX: ";
    typeOut(text, 15000); // Green and typed slowly
    cout << "\033[0m";
}

void showBanner() {
    cout << "\033[1;36m";
    cout << "=========================================\n";
    cout << "        🤖 Welcome to AayuX Chatbot       \n";
    cout << "    Powered by Python + C++ + Curl API   \n";
    cout << "=========================================\n";
    cout << "\033[0m";
    cout << "Type 'exit' to end the conversation.\n\n";
}

int main() {
    string userInput;

    showBanner();

    while (true) {
        cout << "\033[1;34m-----------------------------------------\033[0m\n";
        cout << "\033[1;36mYou: \033[0m";
        getline(cin, userInput);

        if (userInput == "exit") {
            printBot("Goodbye, Mr. Aayush!");
            break;
        }

        CURL* curl;
        CURLcode res;
        string readBuffer;

        // Build JSON payload
        stringstream payload;
        payload << "{\"message\": \"" << userInput << "\"}";

        curl = curl_easy_init();
        if (curl) {
            struct curl_slist* headers = NULL;
            headers = curl_slist_append(headers, "Content-Type: application/json");

            curl_easy_setopt(curl, CURLOPT_URL, "http://127.0.0.1:5000/chat");
            curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
            curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload.str().c_str());
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

            res = curl_easy_perform(curl);
            curl_easy_cleanup(curl);
        }

        string reply = extractReply(readBuffer);
        printBot(reply);
    }

    return 0;
}
