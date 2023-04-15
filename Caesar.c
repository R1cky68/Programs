#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Only works on odd numbered chars rn --> solved, instead of text[i] variable can just print from straight

int main(int argc, string argv[])
{
    // Getting key and converting to integer
    int k = atoi(argv[1]);

    // If inputting too many numbers print error message and quit program
   if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
   }

    // If inputting letters then error
  for (int i = 0; i < strlen(argv[1]); i++)
    {
      if (!isdigit(argv[1][i]))
      {
          printf("Usage: ./caesar key \n");
          return 1;
      }

    }

  // Outputting plain text
    string text = get_string("plaintext: ");
    // printf("%s \n", text);

  // Creating cipher text
  int i = 0;

// Outputting cipher text
  printf("ciphertext: ");

  for (i = 0; i < strlen(text); i++)
  {

    if (isupper(text[i]))
    {
    //  text[i] = (text[i] + k);
    //  i++;
      printf("%c ", text[i] - 65 + k % 26 + 65);

    }

    else if (islower(text[i]))
    {
    // text[i] = (text[i] + k);
     // i++;
      printf("%c ", text[i] - 97 + k % 26 + 97);

    }

}

  printf("\n");

}
