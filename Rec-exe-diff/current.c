#include <stdio.h>
#include <string.h>

int main() {
  FILE *fp;
  char str[] = "This is a test string.";
  char buffer[100];

  fp = fopen("new1.dat", "w");
  if (fp == NULL) {
    perror("Error opening file for writing");
    return 1;
  }
  fprintf(fp, "%s", str);
  fclose(fp);

  fp = fopen("new1.dat", "r");
  if (fp == NULL) {
    perror("Error opening file for reading");
    return 1;
  }
  fgets(buffer, sizeof(buffer), fp);
  printf("%s\n", buffer);
  fclose(fp);

  return 0;
}
