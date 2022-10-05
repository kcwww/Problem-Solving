#include <stdio.h>

int main() {

    int t,num,count=0,ans=0;

  scanf("%d",&t);

  while(t){

    scanf("%d",&num);

    for(int i=1;i<num;i++){

      if((num % i) ==0) count++;

    }

    if(count == 1){

      ans++;

    }

    count=0;

    t--;

  }

  printf("%d",ans);

    return 0;

}

  
