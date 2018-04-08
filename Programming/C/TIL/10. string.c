#include <string.h>
#include <stdio.h>


char str1[20] = "abcdefgh", str2[10] = "abcdfgh";

int main(void) {
	// strlen 문자열의 길이를 안다.
	printf("%d\n",strlen(str1)); // NULL, \0 까지 탐색합니다.

	// strcmp
	// -1 이면 L이 R보다 작다
	// 0 이면 같고
	// 1 이면 R이 L보다 큰 것이다. 그냥 수평선 그려놓고 생각하면 되지 않을까
	printf("%d\n", strcmp(str1, str2));

	// strcat 합친다
	strcat(str1, str2); // str1 의 뒤에 str2를 가져다 붙입니다!! 이것도 \0을 기준으로 동작합니다
	puts(str1);

	// strstr
	// subStr이 있는 곳의 포인터를 반환합니다.
	puts(strstr("hello world is good", "world"));

	// strchr
	// strstr 같이 char가 처음 발견되는 곳을 반환합니다!!
	// TIP : 만약 뒤에서 부터 탐색하고 싶으면 대강 strr___ 형식으로 하면 됩니다.

	// strcpy
	// 이름 그대로 복사합니다 R to L
	strcpy(str1, str2);
	puts(str1);

	// 나머지는 구글링 하면 다 나온다
		
	return 0;
}