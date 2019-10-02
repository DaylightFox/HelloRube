#include <iostream>
#include <string>

using namespace std;

int main()
{
    string pill;
    char decision;

    cout << "Before we get started... do you choose the red or blue pill?" << endl;
    cin >> pill;
    cout << endl;

    if (pill.compare("red") == 0 || pill.compare("Red") == 0 || pill.compare("RED") == 0)
    {
        cout << "Well, that's disappointing...   goodbye" << endl;
        return 0;
    }

    cout << "The '" << pill << "' pill, interesting choice" << endl
         << endl;

    cout << "Are you sure you want to proceed? (Y/N)" << endl;
    cin >> decision;
    cout << endl;

    switch (decision)
    {
    case 'n':
    case 'N':
        cout << "Well, that's disappointing...   goodbye" << endl;
        break;
    case 'y':
    case 'Y':
        cout << "Entering the matrix to find a suitable phrase for your first foray into the world of code ....." << endl;

        cout << "Suitable phrase found." << endl;

        cout << "Hello World!" << endl;
        break;
    default:
        cout << "I'm not sure what you mean to say by typing '" << decision << "', I guess we'll have to try again later." << endl;
    }

    return 0;
}