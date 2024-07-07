import requests
import re
import colorama
import os

os.system('cls' if os.name == 'nt' else 'clear')

colorama.init()
def show_country_list():
    print("""\033[1;32m1) \033[1;33mUnited States                \033[1;32m32) \033[1;33mMexico                \033[1;32m61) \033[1;33mMoldova
\033[1;32m2) \033[1;33mJapan                        \033[1;32m33) \033[1;33mChina                 \033[1;32m62) \033[1;33mNicaragua
\033[1;32m3) \033[1;33mItaly                        \033[1;32m34) \033[1;33mChile                 \033[1;32m63) \033[1;33mMalta
\033[1;32m4) \033[1;33mKorea                        \033[1;32m35) \033[1;33mSouth Africa          \033[1;32m64) \033[1;33mTrinidad And Tobago
\033[1;32m5) \033[1;33mFrance                       \033[1;32m36) \033[1;33mSlovakia              \033[1;32m65) \033[1;33mSoudi Arabia
\033[1;32m6) \033[1;33mGermany                      \033[1;32m37) \033[1;33mHungary               \033[1;32m66) \033[1;33mCroatia
\033[1;32m7) \033[1;33mTaiwan                       \033[1;32m38) \033[1;33mIreland               \033[1;32m67) \033[1;33mCyprus
\033[1;32m8) \033[1;33mRussian Federation           \033[1;32m39) \033[1;33mEgypt                 \033[1;32m68) \033[1;33mPakistan
\033[1;32m9) \033[1;33mUnited Kingdom               \033[1;32m40) \033[1;33mThailand              \033[1;32m69) \033[1;33mUnited Arab Emirates
\033[1;32m10) \033[1;33mNetherlands                 \033[1;32m41) \033[1;33mUkraine               \033[1;32m70) \033[1;33mKazakhstan
\033[1;32m11) \033[1;33mCzech Republic              \033[1;32m42) \033[1;33mSerbia                \033[1;32m71) \033[1;33mKuwait
\033[1;32m12) \033[1;33mTurkey                      \033[1;32m43) \033[1;33mHong Kong             \033[1;32m72) \033[1;33mVenezuela
\033[1;32m13) \033[1;33mAustria                     \033[1;32m44) \033[1;33mGreece                \033[1;32m73) \033[1;33mGeorgia
\033[1;32m14) \033[1;33mSwitzerland                 \033[1;32m45) \033[1;33mPortugal              \033[1;32m74) \033[1;33mMontenegro
\033[1;32m15) \033[1;33mSpain                       \033[1;32m46) \033[1;33mLatvia                \033[1;32m75) \033[1;33mEl Salvador
\033[1;32m16) \033[1;33mCanada                      \033[1;32m47) \033[1;33mSingapore             \033[1;32m76) \033[1;33mLuxembourg
\033[1;32m17) \033[1;33mSweden                      \033[1;32m48) \033[1;33mIceland               \033[1;32m77) \033[1;33mCuracao
\033[1;32m18) \033[1;33mIsrael                      \033[1;32m49) \033[1;33mMalaysia              \033[1;32m78) \033[1;33mPuerto Rico
\033[1;32m19) \033[1;33mIran                        \033[1;32m50) \033[1;33mColombia              \033[1;32m79) \033[1;33mCosta Rica
\033[1;32m20) \033[1;33mPoland                      \033[1;32m51) \033[1;33mTunisia               \033[1;32m80) \033[1;33mBelarus
\033[1;32m21) \033[1;33mIndia                       \033[1;32m52) \033[1;33mEstonia               \033[1;32m81) \033[1;33mAlbania
\033[1;32m22) \033[1;33mNorway                      \033[1;32m53) \033[1;33mDominican Republic    \033[1;32m82) \033[1;33mLiechtenstein
\033[1;32m23) \033[1;33mRomania                     \033[1;32m54) \033[1;33mSloveania             \033[1;32m83) \033[1;33mBosnia And Herzegovia
\033[1;32m24) \033[1;33mViet Nam                    \033[1;32m55) \033[1;33mEcuador               \033[1;32m84) \033[1;33mParaguay
\033[1;32m25) \033[1;33mBelgium                     \033[1;32m56) \033[1;33mLithuania             \033[1;32m85) \033[1;33mPhilippines
\033[1;32m26) \033[1;33mBrazil                      \033[1;32m57) \033[1;33mPalestinian           \033[1;32m86) \033[1;33mGuatemala
\033[1;32m27) \033[1;33mBulgaria                    \033[1;32m58) \033[1;33mNew Zealand           \033[1;32m87) \033[1;33mNepal
\033[1;32m28) \033[1;33mIndonesia                   \033[1;32m59) \033[1;33mBangladeh             \033[1;32m88) \033[1;33mPeru
\033[1;32m29) \033[1;33mDenmark                     \033[1;32m60) \033[1;33mPanama                \033[1;32m89) \033[1;33mUruguay
\033[1;32m30) \033[1;33mArgentina                   \033[1;32m61) \033[1;33mMoldova               \033[1;32m90) \033[1;33mUruguay
\033[1;32m91) \033[1;33mExtra                       \033[1;32m92) \033[1;33mAndorra               \033[1;32m93) \033[1;33mAntigua And Barbuda
\033[1;32m94) \033[1;33mArmenia                     \033[1;32m95) \033[1;33mAngola                \033[1;32m96) \033[1;33mAustralia
\033[1;32m97) \033[1;33mAruba                       \033[1;32m98) \033[1;33mAzerbaijan            \033[1;32m99) \033[1;33mBarbados
\033[1;32m100) \033[1;33mBonaire                    \033[1;32m101) \033[1;33mBahamas              \033[1;32m102) \033[1;33mBotswana
\033[1;32m103) \033[1;33mCongo                      \033[1;32m104) \033[1;33mIvory Coast          \033[1;32m105) \033[1;33mAlgeria
\033[1;32m106) \033[1;33mFiji                       \033[1;32m107) \033[1;33mGabon                \033[1;32m108) \033[1;33mGuernsey
\033[1;32m109) \033[1;33mGreenland                  \033[1;32m110) \033[1;33mGuadeloupe           \033[1;32m111) \033[1;33mGuam
\033[1;32m112) \033[1;33mGuyana                     \033[1;32m113) \033[1;33mHonduras             \033[1;32m114) \033[1;33mJersey
\033[1;32m115) \033[1;33mJamaica                    \033[1;32m116) \033[1;33mJordan               \033[1;32m117) \033[1;33mKenya
\033[1;32m118) \033[1;33mCambodia                   \033[1;32m119) \033[1;33mSaint Kitts          \033[1;32m120) \033[1;33mCayman Islands
\033[1;32m121) \033[1;33mLaos                       \033[1;32m122) \033[1;33mLebanon              \033[1;32m123) \033[1;33mSri Lanka
\033[1;32m124) \033[1;33mMorocco                    \033[1;32m125) \033[1;33mMadagascar           \033[1;32m126) \033[1;33mMacedonia
\033[1;32m127) \033[1;33mMongolia                   \033[1;32m128) \033[1;33mMacao                \033[1;32m129) \033[1;33mMartinique
\033[1;32m130) \033[1;33mMauritius                  \033[1;32m132) \033[1;33mNamibia              \033[1;32m133) \033[1;33mNew Caledonia
\033[1;32m134) \033[1;33mNigeria                    \033[1;32m135) \033[1;33mQatar                \033[1;32m136) \033[1;33mReunion
\033[1;32m137) \033[1;33mSudan                      \033[1;32m138) \033[1;33mSenegal              \033[1;32m139) \033[1;33mSuriname
\033[1;32m140) \033[1;33mSao Tome And Principe      \033[1;32m141) \033[1;33mSyria                \033[1;32m142) \033[1;33mTanzania
\033[1;32m143) \033[1;33mUganda                     \033[1;32m144) \033[1;33mUzbekistan           \033[1;32m145) \033[1;33mSaint Vincent And The Grenadines
""")
    
def main():
    while True:
        show_country_list()

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"
            }

            print(colorama.Fore.GREEN + "[Camera Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the Country Number (type 'exit' to quit):")
            num = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE)

            if num.lower() == 'exit':
                break

            try:
                num = int(num)
                
                if num not in range(1, 146): 
                    raise IndexError("Country number out of range")

                countries = [
                    "US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL", "CZ",
                    "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR", "NO", "RO",
                    "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR", "MX", "FI", "CN",
                    "CL", "ZA", "SK", "HU", "IE", "EG", "TH", "UA", "RS", "HK", "GR",
                    "PT", "LV", "SG", "IS", "MY", "CO", "TN", "EE", "DO", "SI", "EC",
                    "LT", "PS", "NZ", "BD", "PA", "MD", "NI", "MT", "TT", "SA", "HR",
                    "CY", "PK", "AE", "KZ", "KW", "VE", "GE", "ME", "SV", "LU", "CW",
                    "PR", "CR", "BY", "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP",
                    "PE", "UY", "-", "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB",
                    "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL", "GP",
                    "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN", "KY", "LA",
                    "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ", "MU", "NA", "NC",
                    "NG", "QA", "RE", "SD", "SN", "SR", "ST", "SY", "TZ", "UG", "UZ",
                    "VC", "BJ"
                ]
                country = countries[num - 1]
                res = requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
                last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)
                last_page = int(last_page[0]) if last_page else 1  

                found_any_ip = False  

                for page in range(1, last_page + 1):
                    res = requests.get(f"http://www.insecam.org/en/bycountry/{country}/?page={page}", headers=headers)
                    find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)
                    for ip in find_ip:
                        protocol, rest = ip.split("://")
                        ip_address, port = rest.split(":")
                        print(f"{colorama.Fore.CYAN + protocol + '://'}{colorama.Fore.LIGHTCYAN_EX + ip_address}{colorama.Fore.LIGHTCYAN_EX + ':' + port}")
                        found_any_ip = True  

                if not found_any_ip:
                    print(colorama.Fore.GREEN + "[Camera Scanner]: " + colorama.Fore.LIGHTCYAN_EX + "No camera was found in the searched country.")

            except ValueError:
                print(colorama.Fore.GREEN + "[Camera Scanner]: " + colorama.Fore.RED + "Invalid number format. Please enter a valid number.")
            except IndexError:
                print(colorama.Fore.GREEN + "[Camera Scanner]: " + colorama.Fore.RED + "Country number out of range. Please enter a number between 1 and 145.")
            except Exception as e:
                print(colorama.Fore.RED + str(e))

            finally:
                try:
                    input(colorama.Fore.GREEN + "[Camera Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")
                except KeyboardInterrupt:
                    continue

                os.system('cls' if os.name == 'nt' else 'clear')
    
        except Exception as e:
            print(colorama.Fore.RED + str(e))

if __name__ == "__main__":
    main()
