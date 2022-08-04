#define _CRT_SECURE_MO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
    char arr[100] = {0,};
    scanf("%s", arr);
    int count=0;
  for(int i=0; i<strlen(arr);i++){
    if(arr[i]=='c'){
      if(arr[i+1]=='-') count++;
      else if(arr[i+1]=='=') count++;
        }

    else if(arr[i]=='d'){
      if(arr[i+1]=='-') count++;
      else if((arr[i+1]=='z') && (arr[i+2] == '=')) count++;
        }

    else if(arr[i]=='l'){
      if(arr[i+1]=='j') count++;
      
        }

    else if(arr[i]=='n'){
      if(arr[i+1]=='j') count++;
      
        }

    else if(arr[i]=='s'){
      if(arr[i+1]=='=') count++;
      
        }

    else if(arr[i]=='z'){
      if(arr[i+1]=='=') count++;
      
        }

    

    
  }
  
  printf("%d", strlen(arr) - count);
    return 0;
}
