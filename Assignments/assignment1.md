# Bài tập 1

*Sinh viên thực hiện: Nguyễn Anh Tú - 20184000*

## Bản mã ban đầu

```
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb

```

## Chương trình tính tần suất các ký tự từ `a` đến `z`

```c++
#include <bits/stdc++.h>

using namespace std;

int main()
{
	string ciphertext;
	ifstream MyFile("ciphertext.txt");
	if (!MyFile.is_open())
	{
		cout << "Can't read file.";
	}
	else
	{
		ciphertext = string((istreambuf_iterator<char>(MyFile)), istreambuf_iterator<char>());

		map<char, int> charFreq;
		for (char c : ciphertext)
		{
			if (c >= 'a' && c <= 'z')
			{
				charFreq[c]++;
			}
		}
		// sort charFreq by value
		vector<pair<char, int>> arr(0);
		for (pair<char, int> p : charFreq)
		{
			arr.push_back(p);
		}
		for (int i = 0; i < arr.size() - 1; ++i)
		{
			for (int j = i + 1; j < arr.size(); ++j)
			{
				if (arr[i].second < arr[j].second)
				{
					pair<char, int> tmp = arr[i];
					arr[i] = arr[j];
					arr[j] = tmp;
				}
			}
		}
		double sum = 0;
		for (pair<char, int> p : arr)
		{
			sum += p.second;
		}
		for (pair<char, int> p : arr)
		{
			cout << p.first << ": " << (double)p.second / sum << endl;
		}
	}

	MyFile.close();
	return 0;
}

```

Kết quả sau khi chạy chương trình:

|  r   |  b   |  m   |  k   |  j   |  w   |  i   |  p   |  u   |  d   |  h   |  v   | x    |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | ---- |
| .130 | .105 | .096 | .076 | .074 | .073 | .063 | .046 | .037 | .036 | .036 | .034 | .031 |

|  y   |  s   |  n   |  t   |  l   |  o   |  q   |  c   |  a   |  e   |  f   |  g   |  z   |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| .029 | .026 | .026 | .020 | .012 | .011 | .011 | .008 | .008 | .008 | .002 | .002 | .000 |

## Giải mã bằng phân tích tần suất

Trạng thái ban đầu:

```
lrvmnir bpr sumvbwvr jx bpr lmiwv 
yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt     

wb wi kjb mk rmit bmiq bj rashmwk 
rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk 
nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
```

Ký tự `r` có tần suất lớn nhất. Thay `r = E`.

`bpr` xuất hiện 11 lần. Từ có dạng `bpE` trong tiếng Anh phổ biến nhất là `THE`. Vậy `b = T`, `p = H`. Kết luận này phù hợp với tần suất của ký tự `T`, cao thứ hai sau `E` trong tiếng Anh.

```
lEvmniE THE sumvTwvE jx THE lmiwv 
yjeEyEkTi jx qmTm wi
THE xjvni mkd ymiTEut jx iEhx wi THE EiiEkvE jx
ymTinlmtmiHw utn qmumTE dj w iHmhh Tut Tj EhnvwdmTE THE
yjeEyEkTi jx THE qmTm mvvjudwko Tj yt wkTEusuETmTwjk
lmiEd jk xjuTt tEmui jx iTndt     

wT wi kjT mk Emit Tmiq Tj Eashmwk 
EmvH yjeEyEkT mkd wTi
iwokwxwvmkvE mkd ijyE yniT uEymwk 
nkEashmwkEd Tj oweE m
vjyshETE EashmkmTwjk jkE cjnhd HmeE Tj lE fnmhwxwEd mkd
wkiswuEd Tj invH mk EaTEkT THmT HE vjnhd uEmvH THE iTmTE
jx EkhwoHTEkEd ywkd vmsmlhE jx uEvjokwgwko ijnkdhEii
ijnkd mkd iHmsEhEii iHmsE w dj kjT dEEy ytiEhx THE xwkmh
mnTHjuwTt lnT yt EasEuwEkvE cwTH qmTm Hmi hExT kj djnlT
THmT THE xjhhjcwko wi THE sujsEu msshwvmTwjk mkd
wkTEusuETmTwjk w jxxEu yt THEjuwEi wk THE HjsE THmT THE
EiiEkvE jx jqwkmcmk qmumTE cwhh uEymwk wkTmvT
```

Để ý ở dòng 1, `jx` đứng ngay trước `THE`. Vậy khả năng cao `jx = OF`, phù hợp với tần suất đã khảo sát.

Dòng 12 có từ `lE`, với tần suất đã khảo sát mạnh dạn dự đoán là `BE`. 2 trường hợp khác có thể xảy ra là `HE` hoặc `ME`, nhưng tần suất trong tiếng Anh không phù hợp. Vậy `l = B`.

Ở dòng 13 có từ `THmT`, có thể là `THOT` hoặc `THAT`. Em hy vọng là trường hợp 2 =)) `m = A`.

```
BEvAniE THE suAvTwvE OF THE BAiwv 
yOeEyEkTi OF qATA wi
THE FOvni Akd yAiTEut OF iEhF wi THE EiiEkvE OF
yATinBAtAiHw utn qAuATE dO w iHAhh Tut TO EhnvwdATE THE
yOeEyEkTi OF THE qATA AvvOudwko TO yt wkTEusuETATwOk
BAiEd Ok FOuTt tEAui OF iTndt     

wT wi kOT Ak EAit TAiq TO EashAwk 
EAvH yOeEyEkT Akd wTi
iwokwFwvAkvE Akd iOyE yniT uEyAwk 
nkEashAwkEd TO oweE A
vOyshETE EashAkATwOk OkE cOnhd HAeE TO BE fnAhwFwEd Akd
wkiswuEd TO invH Ak EaTEkT THAT HE vOnhd uEAvH THE iTATE
OF EkhwoHTEkEd ywkd vAsABhE OF uEvOokwgwko iOnkdhEii
iOnkd Akd iHAsEhEii iHAsE w dO kOT dEEy ytiEhF THE FwkAh
AnTHOuwTt BnT yt EasEuwEkvE cwTH qATA HAi hEFT kO dOnBT
THAT THE FOhhOcwko wi THE suOsEu AsshwvATwOk Akd
wkTEusuETATwOk w OFFEu yt THEOuwEi wk THE HOsE THAT THE
EiiEkvE OF OqwkAcAk qAuATE cwhh uEyAwk wkTAvT
```

Dòng 16, `EasEuwEkvE` chỉ có thể là `EXPERIENCE`.  Các tần suất hoàn toàn phù hợp.

```
BECAniE THE PRACTICE OF THE BAiIC 
yOeEyENTi OF qATA Ii
THE FOCni ANd yAiTERt OF iEhF Ii THE EiiENCE OF
yATinBAtAiHI Rtn qARATE dO I iHAhh TRt TO EhnCIdATE THE
yOeEyENTi OF THE qATA ACCORdINo TO yt INTERPRETATION
BAiEd ON FORTt tEARi OF iTndt     

IT Ii NOT AN EAit TAiq TO EXPhAIN 
EACH yOeEyENT ANd ITi
iIoNIFICANCE ANd iOyE yniT REyAIN 
nNEXPhAINEd TO oIeE A
COyPhETE EXPhANATION ONE cOnhd HAeE TO BE fnAhIFIEd ANd
INiPIREd TO inCH AN EXTENT THAT HE COnhd REACH THE iTATE
OF ENhIoHTENEd yINd CAPABhE OF RECOoNIgINo iOnNdhEii
iOnNd ANd iHAPEhEii iHAPE I dO NOT dEEy ytiEhF THE FINAh
AnTHORITt BnT yt EXPERIENCE cITH qATA HAi hEFT NO dOnBT
THAT THE FOhhOcINo Ii THE PROPER APPhICATION ANd
INTERPRETATION I OFFER yt THEORIEi IN THE HOPE THAT THE
EiiENCE OF OqINAcAN qARATE cIhh REyAIN INTACT
```

Dòng 8, `IT Ii NOT AN` chỉ có thể là `i = S`. Cũng dòng đó, `EXPhAIN = EXPLAIN`.

Dòng 12, `ANd` có thể là `AND` hoặc `ANT`.  `AND` thường xuyên xuất hiện trong tiếng Anh, cộng với tần suất khá chính xác, vậy `d = D`.

Dòng cuối cùng, `REyAIN = REMAIN`.

```
BECAnSE THE PRACTICE OF THE BASIC 
MOeEMENTS OF qATA IS
THE FOCnS AND MASTERt OF SELF IS THE ESSENCE OF
MATSnBAtASHI Rtn qARATE DO I SHALL TRt TO ELnCIDATE THE
MOeEMENTS OF THE qATA ACCORDINo TO Mt INTERPRETATION
BASED ON FORTt tEARS OF STnDt     

IT IS NOT AN EASt TASq TO EXPLAIN 
EACH MOeEMENT AND ITS
SIoNIFICANCE AND SOME MnST REMAIN 
nNEXPLAINED TO oIeE A
COMPLETE EXPLANATION ONE cOnLD HAeE TO BE fnALIFIED AND
INSPIRED TO SnCH AN EXTENT THAT HE COnLD REACH THE STATE
OF ENLIoHTENED MIND CAPABLE OF RECOoNIgINo SOnNDLESS
SOnND AND SHAPELESS SHAPE I DO NOT DEEM MtSELF THE FINAL
AnTHORITt BnT Mt EXPERIENCE cITH qATA HAS LEFT NO DOnBT
THAT THE FOLLOcINo IS THE PROPER APPLICATION AND
INTERPRETATION I OFFER Mt THEORIES IN THE HOPE THAT THE
ESSENCE OF OqINAcAN qARATE cILL REMAIN INTACT
```

Đến đây, ta có thể dễ dàng đọc - hiểu và giải mã các ký tự còn lại.

`e = V`, `c = W`, `n = U`, `t = Y`, `o = G`, `q = K`, `f = Q`, `g = Z`.

Ký tự duy nhất không xuất hiện trong bản mã là `z = J`.

Kết quả cuối cùng:

```
BECAUSE THE PRACTICE OF THE BASIC 
MOVEMENTS OF KATA IS
THE FOCUS AND MASTERY OF SELF IS THE ESSENCE OF
MATSUBAYASHI RYU KARATE DO I SHALL TRY TO ELUCIDATE THE
MOVEMENTS OF THE KATA ACCORDING TO MY INTERPRETATION
BASED ON FORTY YEARS OF STUDY     

IT IS NOT AN EASY TASK TO EXPLAIN 
EACH MOVEMENT AND ITS
SIGNIFICANCE AND SOME MUST REMAIN 
UNEXPLAINED TO GIVE A
COMPLETE EXPLANATION ONE WOULD HAVE TO BE QUALIFIED AND
INSPIRED TO SUCH AN EXTENT THAT HE COULD REACH THE STATE
OF ENLIGHTENED MIND CAPABLE OF RECOGNIZING SOUNDLESS
SOUND AND SHAPELESS SHAPE I DO NOT DEEM MYSELF THE FINAL
AUTHORITY BUT MY EXPERIENCE WITH KATA HAS LEFT NO DOUBT
THAT THE FOLLOWING IS THE PROPER APPLICATION AND
INTERPRETATION I OFFER MY THEORIES IN THE HOPE THAT THE
ESSENCE OF OKINAWAN KARATE WILL REMAIN INTACT
```

Chìa khóa giải mã:

|  r   |  b   |  m   |  k   |  j   |  w   |  i   |  p   |  u   |  d   |  h   |  v   | x    |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | ---- |
|  e   |  t   |  a   |  n   |  o   |  i   |  s   |  h   |  r   |  d   |  l   |  c   | f    |

|  y   |  s   |  n   |  t   |  l   |  o   |  q   |  c   |  a   |  e   |  f   |  g   |  z   |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  m   |  p   |  u   |  y   |  b   |  g   |  k   |  w   |  x   |  v   |  q   |  z   |  j   |

## Ai đã viết văn bản này?

Nagamine Shōshin, 1998. *The Essence of Okinawan Karate-Do*. Tuttle Publishing.

## Tài liệu tham khảo
