from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pickle
from tkinter import messagebox
import webbrowser
import pymysql
import pygame

window = Tk()
window.title('Login Page')
window.geometry('1397x800')
 
#BG Image
canvas = Canvas(window,height=800,width=1397)
image_file = ImageTk.PhotoImage(file='C:\\Users\\User\\OneDrive\\Pictures\\images\\nocrime.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack()
 
#Login Frame
frame_login = Frame(window,bg='white')
frame_login.place(x=800,y=70,height=500,width=500)
 
#title
title = Label(frame_login,text='Login',font=('Times New Roman',35,'bold'),fg='#3077cc',bg='white')
title.place(x=190,y=20)
 
#email
email = Label(frame_login,text='Email Address :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
email.place(x=50,y=120)
text_email = Entry(frame_login,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
text_email.place(x=50,y=150,width=400,height=35)

#password
password = Label(frame_login,text='Password :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
password.place(x=50,y=210)
text_password = Entry(frame_login,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf',show='*')
text_password.place(x=50,y=240,width=400,height=35)

#register Frame
frame_register = Frame(window,bg='white')
frame_register.place(x=800,y=620,height=100,width=500)

#new user
newuser = Label(frame_register,text='New user?',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
newuser.place(x=125,y=35)


                     

#5 crime news details pages
def cc_page():
   window_cc = Tk()
   window_cc.title('Cybercrimes')
   window_cc.geometry('1397x800')
   window_cc.configure(bg='light blue')

   title = Label(window_cc,text='Cybercrimes',font=('Times New Roman',35,'bold'),fg='black',bg='light blue')
   title.place(x=550,y=30)

   frame_cc1 = LabelFrame(window_cc,text='News 1',font=('Times New Roman',12,'bold'),bg='white')
   frame_cc1.place(x=60,y=200,height=140,width=1000)

   Label(frame_cc1,text='Sudden spike in cybercrime cases in Selangor this year, says state CID chief',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_cc1,text='Tuesday, 14 Sep 2021 06:27 PM MYT',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_cc1,text='SHAH ALAM, Sept 14 ― A total of 380 cyber crime cases were reported in Selangor to date, a sudden increase compared with only 51 cases reported ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_cc1,text='last year especially cases ninvolving pornographic extortion cases, says state CID chief SAC Nik Ezanee Mohd Faisal.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)
   def cc_news1():
       webbrowser.open('https://www.malaymail.com/news/malaysia/2021/09/14/sudden-spike-in-cybercrime-cases-in-selangor-this-year-says-state-cid-chief/2005526')

   frame_cc1_button = Button(window_cc,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=cc_news1)
   frame_cc1_button.place(x=1100,y=250)

   frame_cc2 = LabelFrame(window_cc,text='News 2',font=('Times New Roman',12,'bold'),bg='white')
   frame_cc2.place(x=60,y=400,height=140,width=1000)

   Label(frame_cc2,text='15,935 online fraud cases, RM380mil in losses in first 9 months of 2021',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_cc2,text='October 27, 2021 11:52 PM',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_cc2,text='KUALA LUMPUR: A total of 15,935 online cheating cases with losses amounting to about RM380 million were recorded in the first ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_cc2,text='nine months of this year, according to Bukit Aman’s commercial crime investigation department (CCID).',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)

   def cc_news2():
       webbrowser.open('https://www.freemalaysiatoday.com/category/nation/2021/10/27/15935-online-fraud-cases-rm380mil-in-losses-in-first-9-months-of-2021/')
       
   frame_cc2_button = Button(window_cc,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=cc_news2)
   frame_cc2_button.place(x=1100,y=450)

   frame_cc3 = LabelFrame(window_cc,text='News 3',font=('Times New Roman',12,'bold'),bg='white')
   frame_cc3.place(x=60,y=600,height=140,width=1000)

   Label(frame_cc3,text='Cybercrimes went up 99% in 2020',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_cc3,text='Friday, November 26th, 2021 ',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_cc3,text='CYBERCRIME complaints increased by 99.5% to 20,805 last year from 10,426 in 2019, according to the crime statistics from the ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_cc3,text='Department of Statistics Malaysia (DoSM).',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)

   def cc_news3():
       webbrowser.open('https://themalaysianreserve.com/2021/11/26/cybercrimes-went-up-99-in-2020/')
       
   frame_cc3_button = Button(window_cc,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=cc_news3)
   frame_cc3_button.place(x=1100,y=650)


   
def ca_page():
   window_ca = Tk()
   window_ca.title('Child Abuse')
   window_ca.geometry('1397x800')
   window_ca.configure(bg='light blue')

   title = Label(window_ca,text='Child Abuse',font=('Times New Roman',35,'bold'),fg='black',bg='light blue')
   title.place(x=550,y=30)

   frame_ca1 = LabelFrame(window_ca,text='News 1',font=('Times New Roman',12,'bold'),bg='white')
   frame_ca1.place(x=60,y=200,height=140,width=1000)

   Label(frame_ca1,text='Nearly 1,100 cases of child abuse reported in Selangor from Jan-Sept',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_ca1,text='Wednesday, 01 Dec 2021 03:40 PM MYT',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_ca1,text='SHAH ALAM, Dec 1 — A total of 1,076 child abuse cases were reported in the state from January to September this year, the Selangor ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_ca1,text='state legislative assembly was told today.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def ca_news1():
       webbrowser.open('https://www.malaymail.com/news/malaysia/2021/12/01/nearly-1100-cases-of-child-abuse-reported-in-selangor-from-jan-sept-state-a/2025133')

   frame_ca1_button = Button(window_ca,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=ca_news1)
   frame_ca1_button.place(x=1100,y=250)

   frame_ca2 = LabelFrame(window_ca,text='News 2',font=('Times New Roman',12,'bold'),bg='white')
   frame_ca2.place(x=60,y=400,height=140,width=1000)

   Label(frame_ca2,text='‘Angry’ Dads & Women Responsible For Majority Of Child Abuse Cases In 2021',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_ca2,text='OCTOBER 11, 2021',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_ca2,text='Police’s D11 Sexual, Women and Child Investigations Division reveal that adults with anger issues, coupled with a very short fuse, ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_ca2,text='were responsible for a total of 472 child abuse incidents that were reported within the first nine months of 2021.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def ca_news2():
       webbrowser.open('https://www.therakyatpost.com/news/2021/10/11/angry-dads-women-responsible-for-majority-of-child-abuse-cases-in-2021/')

   frame_ca2_button = Button(window_ca,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=ca_news2)
   frame_ca2_button.place(x=1100,y=450)

   frame_ca3 = LabelFrame(window_ca,text='News 3',font=('Times New Roman',12,'bold'),bg='white')
   frame_ca3.place(x=60,y=600,height=140,width=1000)

   Label(frame_ca3,text='Child abuse, a never ending story',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_ca3,text='February 1, 2021 @ 5:22pm',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_ca3,text='LETTER: Malaysia was shocked once again during this MCO season by the story of child violence resulting in death. Zubaidi Amir, 7',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_ca3,text='was reported dead by his step-father, due to drowning in a tub.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def ca_news3():
       webbrowser.open('https://www.nst.com.my/opinion/letters/2021/02/662168/child-abuse-never-ending-story')

   frame_ca3_button = Button(window_ca,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=ca_news3)
   frame_ca3_button.place(x=1100,y=650)

   
def rp_page():
   window_rp = Tk()
   window_rp.title('Rape')
   window_rp.geometry('1397x800')
   window_rp.configure(bg='light blue')

   title = Label(window_rp,text='Rape',font=('Times New Roman',35,'bold'),fg='black',bg='light blue')
   title.place(x=550,y=30)

   frame_rp1 = LabelFrame(window_rp,text='News 1',font=('Times New Roman',12,'bold'),bg='white')
   frame_rp1.place(x=60,y=200,height=140,width=1000)

   Label(frame_rp1,text='Rape cases in Kelantan increase during MCO period',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_rp1,text='September 5, 2021 @ 6:20pm',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_rp1,text='BACHOK: Police recorded a drastic increase of 51 alleged rape cases in the first seven months of this year following the implementation of the',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_rp1,text='Movement Control Order (MCO).',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)

   def rp_news1():
       webbrowser.open('https://www.nst.com.my/news/crime-courts/2021/09/724567/rape-cases-kelantan-increase-during-mco-period')

   frame_rp1_button = Button(window_rp,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=rp_news1)
   frame_rp1_button.place(x=1100,y=250)

   frame_rp2 = LabelFrame(window_rp,text='News 2',font=('Times New Roman',12,'bold'),bg='white')
   frame_rp2.place(x=60,y=400,height=140,width=1000)

   Label(frame_rp2,text='Cops hunting two men who allegedly spiked drink, raped teenager',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_rp2,text='Saturday, 20 Nov 2021 11:37 AM MYT',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_rp2,text='Based on the report, the 19-year-old victim alleged that she went to a nightclub with a few friends at about 9pm on Wednesday (Nov 17). ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_rp2,text='The victim was intoxicated after her drink was spiked with drugs," he said in a statement on Saturday (Nov 20).',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def rp_news2():
       webbrowser.open('https://www.thestar.com.my/news/nation/2021/11/20/cops-hunting-two-men-who-allegedly-spiked-drink-raped-teenager')

   frame_rp2_button = Button(window_rp,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=rp_news2)
   frame_rp2_button.place(x=1100,y=450)

   frame_rp3 = LabelFrame(window_rp,text='News 3',font=('Times New Roman',12,'bold'),bg='white')
   frame_rp3.place(x=60,y=600,height=140,width=1000)

   Label(frame_rp3,text='The 17-year-old exposing rape culture in Malaysian schools',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_rp3,text='19 May 2021',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_rp3,text='Kuala Lumpur, Malaysia – When a 17-year-old Malaysian student went on TikTok to call out her physical education teacher for a “rape joke” he shared ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_rp3,text='in front of the class in late April,it triggered a firestorm of debate but also a backlash against the teen in the Muslim-majority country.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def rp_news3():
       webbrowser.open('https://www.aljazeera.com/news/2021/5/19/the-17-year-old-exposing-rape-culture-in-malaysian-schools')

   frame_rp3_button = Button(window_rp,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=rp_news3)
   frame_rp3_button.place(x=1100,y=650)

   
   
def bg_page():
   window_bg = Tk()
   window_bg.title('Burglary')
   window_bg.geometry('1397x800')
   window_bg.configure(bg='light blue')

   title = Label(window_bg,text='Burglary',font=('Times New Roman',35,'bold'),fg='black',bg='light blue')
   title.place(x=550,y=30)

   frame_bg1 = LabelFrame(window_bg,text='News 1',font=('Times New Roman',12,'bold'),bg='white')
   frame_bg1.place(x=60,y=200,height=150,width=1000)

   Label(frame_bg1,text='Most burglary suspects during MCO were jobless, say cops',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_bg1,text='June 29, 2021 3:40 PM',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_bg1,text='KUALA LUMPUR: Almost two-thirds of suspects arrested over house burglaries during the movement control order period were those without jobs, police said.',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_bg1,text='Criminal Investigation Department director Abd Jalil Hassan said a total of 5,518 individuals were arrested during the MCO period between March 18 and June 27,',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)
   Label(frame_bg1,text=' and of the number, 3,572 people were unemployed.',
         font=('Times New Roman',12),bg='white').grid(row=4,column=0,sticky=W)


   def bg_news1():
       webbrowser.open('https://www.freemalaysiatoday.com/category/nation/2021/06/29/most-burglary-suspects-during-mco-were-jobless-say-cops/')

   frame_bg1_button = Button(window_bg,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=bg_news1)
   frame_bg1_button.place(x=1100,y=250)

   frame_bg2 = LabelFrame(window_bg,text='News 2',font=('Times New Roman',12,'bold'),bg='white')
   frame_bg2.place(x=60,y=400,height=150,width=1000)

   Label(frame_bg2,text='Two robbers without face masks nabbed after Malaysian victims easily identify them',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_bg2,text='DEC 1, 2020, 9:45 PM SGT',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_bg2,text='KUALA LUMPUR (THE STAR/ASIA NEWS NETWORK) - Two burglars who broke into two homes in Kuala Lumpur on Sunday (Nov 29) without wearing  ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_bg2,text='face masks were easily identified by their victims later.Police were on alert after two burglars killed one of their victims after breaking into a bungalow',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)
   Label(frame_bg2,text=' in upscale Bangsar in the wee hours of Sunday.',
         font=('Times New Roman',12),bg='white').grid(row=4,column=0,sticky=W)

   def bg_news2():
       webbrowser.open('https://www.straitstimes.com/asia/se-asia/two-burglars-nailed-by-malaysian-victims-after-robbing-houses-without-wearing-face')

   frame_bg2_button = Button(window_bg,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=bg_news2)
   frame_bg2_button.place(x=1100,y=450)

   frame_bg3 = LabelFrame(window_bg,text='News 3',font=('Times New Roman',12,'bold'),bg='white')
   frame_bg3.place(x=60,y=600,height=140,width=1000)

   Label(frame_bg3,text='Yong Gang busted as police solve 30 burglary cases around PJ, Serdang, Brickfields',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_bg3,text='Friday, 27 Nov 2020 09:00 AM MYT',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_bg3,text='SERDANG, Nov 27 ― The police have solved 30 cases of break-ins, including at convenience shops, around Serdang, Brickfields and Petaling Jaya',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_bg3,text='with the arrest of four ”Yong Gang” members.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def bg_news3():
       webbrowser.open('https://www.malaymail.com/news/malaysia/2020/11/27/yong-gang-busted-as-police-solve-30-burglary-cases-around-pj-serdang-brickf/1926563')

   frame_bg3_button = Button(window_bg,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=bg_news3)
   frame_bg3_button.place(x=1100,y=650)

   
def dg_page():
   window_dg = Tk()
   window_dg.title('Drugs')
   window_dg.geometry('1397x800')
   window_dg.configure(bg='light blue')

   title = Label(window_dg,text='Drugs',font=('Times New Roman',35,'bold'),fg='black',bg='light blue')
   title.place(x=550,y=30)

   frame_dg1 = LabelFrame(window_dg,text='News 1',font=('Times New Roman',12,'bold'),bg='white')
   frame_dg1.place(x=60,y=200,height=140,width=1000)

   Label(frame_dg1,text='Johor police to investigate students involved in drug abuse',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_dg1,text='Monday, 14 Sep 2020 04:13 PM MYT',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_dg1,text='JOHOR BARU, Sept 14 — Johor police will investigate claims by the National Anti-Drug Agency (AADK) that there are 177 Form Four and Five students',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_dg1,text='in drug abuse in the state.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def dg_news1():
       webbrowser.open('https://www.malaymail.com/news/malaysia/2020/09/14/johor-police-to-investigate-students-in-drug-abuse/1903116')

   frame_dg1_button = Button(window_dg,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=dg_news1)
   frame_dg1_button.place(x=1100,y=250)

   frame_dg2 = LabelFrame(window_dg,text='News 2',font=('Times New Roman',12,'bold'),bg='white')
   frame_dg2.place(x=60,y=400,height=140,width=1000)

   Label(frame_dg2,text='KL cops nab four drug trafficking suspects',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_dg2,text='November 18, 2021 11:53 PM',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_dg2,text='KUALA LUMPUR: Police have arrested four men on suspicion of being involved in two drug trafficking syndicates operating in the Klang Valley.',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_dg2,text='The suspects, in their 20s to 30s, were arrested in several raids which saw more than RM1.7 million in property and drugs seized.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def dg_news2():
       webbrowser.open('https://www.freemalaysiatoday.com/category/nation/2021/11/18/kl-cops-nab-four-drug-trafficking-suspects/')

   frame_dg2_button = Button(window_dg,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=dg_news2)
   frame_dg2_button.place(x=1100,y=450)

   frame_dg3 = LabelFrame(window_dg,text='News 3',font=('Times New Roman',12,'bold'),bg='white')
   frame_dg3.place(x=60,y=600,height=140,width=1000)

   Label(frame_dg3,text='Malaysia sees rising drug abuse as COVID-19 pandemic drags on | Video',font=('Times New Roman',14,'bold','underline'),bg='white').grid(row=0,column=0,sticky=W)
   Label(frame_dg3,text='09 Sep 2021 10:04pm',font=('Times New Roman',8),bg='white').grid(row=1,column=0,stick=W)
   Label(frame_dg3,text='The disruption of drug rehabilitation programmes caused by the COVID-19 pandemic has resulted in some users relapsing. Melissa Goh finds out how authorities in ',
         font=('Times New Roman',12),bg='white').grid(row=2,column=0,sticky=W)
   Label(frame_dg3,text='Kuala Lumpur are dealing with a rise in substance abuse cases.',
         font=('Times New Roman',12),bg='white').grid(row=3,column=0,sticky=W)


   def dg_news3():
       webbrowser.open('https://www.channelnewsasia.com/watch/malaysia-sees-rising-drug-abuse-covid-19-pandemic-drags-video-2167261')

   frame_dg3_button = Button(window_dg,text='More Info >>>',font=('Times New Roman',15,'bold'),borderwidth=0,bg='light blue',fg='black',command=dg_news3)
   frame_dg3_button.place(x=1100,y=650)


#main page
def main_page():
   window_main = Tk()
   window_main.title('Main page')
   window_main.geometry('1397x800')
   window_main.configure(bg='#6c8ab0')


   #title
   title = Label(window_main,text='Welcome to XCrime',font=('Times New Roman',40,'bold'),fg='white',bg='#6c8ab0')
   title.place(x=450,y=30)

   #Crime news button
   crimenews_button = Button(window_main,text='Crime News',font=('Times New Roman',15,'bold'),borderwidth=8,bg='light blue',command=crimenews_page)
   crimenews_button.place(x=100,y=280,height=250,width=250)
   
   #crime awareness button
   crimeawareness_button = Button(window_main,text='Crime Awareness',font=('Times New Roman',15,'bold'),borderwidth=8,bg='white',command=crimeawareness_page)
   crimeawareness_button.place(x=400,y=280,height=250,width=250)

   #emergency button
   emergency_button = Button(window_main,text='Emergency Contact',font=('Times New Roman',15,'bold'),borderwidth=8,bg='#b31603',command=emergency_page)
   emergency_button.place(x=700,y=280,height=250,width=250)

   #discussion button
   discussion_button = Button(window_main,text='Discussion Board',font=('Times New Roman',15,'bold'),borderwidth=8,bg='#145616',fg='black',command=discussion_page)
   discussion_button.place(x=1000,y=280,height=250,width=250)

   # Initialize mixer module in pygame
   pygame.mixer.init()
   def sound():
       pygame.mixer.music.load('C:\\Users\\User\\Downloads\\mixkit-alert-alarm-1005.wav')
       pygame.mixer.music.play(loops=-1)
       sound_button.config(bg='grey')
   def stop():
      pygame.mixer.music.stop()
      sound_button.config(bg='red')

   sound_button=1
   sound_button = Button(window_main,text='Emergency\nSound',font=('Times New Roman',10,'bold'),borderwidth=5,bg='red',fg='black',command=sound)
   sound_button.place(x=1220,y=700,height=80,width=80)
   stop_button = Button(window_main,text='Stop\nSound',font=('Times New Roman',10,'bold'),borderwidth=5,bg='red',fg='black',command=stop)
   stop_button.place(x=1130,y=700,height=80,width=80)

   def logout():
       window_main.destroy()
       messagebox.showinfo(title='Thank you', message='Logout Successful')
   logout_button = Button(window_main,text='Log Out',font=('Times New Roman',10,'bold'),borderwidth=5,fg='black',command=logout)
   logout_button.place(x=1250,y=40,height=50,width=90)

   window.destroy()
   

#5 categories crimenews
def crimenews_page():
   window_crimen = Tk()
   window_crimen.title('5 Categories Of Crimes News Page')
   window_crimen.geometry('1397x800')
   window_crimen.configure(bg='light blue')


   #title
   title = Label(window_crimen,text='5 Categories Of Crimes News',font=('Times New Roman',35,'bold'),fg='white',bg='light blue')
   title.place(x=450,y=30)
   
   #cybercrimes button
   cybercrimes_button = Button(window_crimen,text='Cybercrimes',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=cc_page)
   cybercrimes_button.place(x=180,y=180,height=60,width=620)

   #child abuse button
   childabuse_button = Button(window_crimen,text='Child Abuse',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=ca_page)
   childabuse_button.place(x=570,y=270,height=60,width=620)

   #rape button
   rape_button = Button(window_crimen,text='Rape',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=rp_page)
   rape_button.place(x=180,y=360,height=60,width=620)

   #burglary button
   burglary_button = Button(window_crimen,text='Burglary',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=bg_page)
   burglary_button.place(x=570,y=450,height=60,width=620)

   #drugs button
   drugs_button = Button(window_crimen,text='Drugs',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=dg_page)
   drugs_button.place(x=180,y=540,height=60,width=620)

   
   

#5 categories crime awareness
def crimeawareness_page():
   window_crimeaware = Tk()
   window_crimeaware.title('5 Categories Of Crimes Awreness Page')
   window_crimeaware.geometry('1397x800')
   window_crimeaware.configure(bg='black')


   #title
   title = Label(window_crimeaware,text='5 Categories Of Crimes Awareness',font=('Times New Roman',35,'bold'),fg='white',bg='black')
   title.place(x=450,y=30)

   def cc_awr():
       webbrowser.open('https://us.norton.com/internetsecurity-how-to-how-to-recognize-and-protect-yourself-from-cybercrime.html')
       
   #cybercrimes button
   cybercrimes_button = Button(window_crimeaware,text='Cybercrimes',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=cc_awr)
   cybercrimes_button.place(x=180,y=180,height=60,width=620)

   def ca_awr():
       webbrowser.open('https://www.cheriehearts.com.my/prevent-child-abuse')
       
   #child abuse button
   childabuse_button = Button(window_crimeaware,text='Child Abuse',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=ca_awr)
   childabuse_button.place(x=570,y=270,height=60,width=620)

   def rp_awr():
       webbrowser.open('https://www.cityofsacramento.org/Police/Resources/Safety-and-Crime-Prevention-Tips/Rape-Prevention')
       
   #rape button
   rape_button = Button(window_crimeaware,text='Rape',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=rp_awr)
   rape_button.place(x=180,y=360,height=60,width=620)

   def bg_awr():
       webbrowser.open('https://www.hg.org/legal-articles/what-elements-must-be-proven-to-secure-a-burglary-conviction-44596')
   #burglary button
   burglary_button = Button(window_crimeaware,text='Burglary',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=bg_awr)
   burglary_button.place(x=570,y=450,height=60,width=620)

   def dg_awr():
       webbrowser.open('https://www.pvamu.edu/sa/drug-and-alcohol-abuse-prevention-program-daapp/tips-for-preventing-substance-abuse/')
   #drugs button
   drugs_button = Button(window_crimeaware,text='Drugs',font=('Times New Roman',20,'bold'),borderwidth=10,bg='white',fg='black',command=dg_awr)
   drugs_button.place(x=180,y=540,height=60,width=620)

   

#Emergency Contact page
def emergency_page():
   window_emergency = Tk()
   window_emergency.title('Emergency Contact Page')
   window_emergency.geometry('1397x800')
   window_emergency.configure(bg='red')

   frame_emergency = Frame(window_emergency,bg='white')
   frame_emergency.place(x=180,y=180,height=200,width=1000)

   title = Label(window_emergency,text='Emergency Contact ',font=('Times New Roman',35,'bold'),fg='black',bg='red')
   title.place(x=480,y=30)

   malaysianum = Label(frame_emergency,text='Malaysia Emergency Number',font=('Times New Roman',25,'bold'),fg='black',bg='white')
   malaysianum.place(x=300,y=20)
   nineninenine = Label(frame_emergency,text='999/112(Mobile)',font=('Times New Roman',30,'bold'),fg='red',bg='white')
   nineninenine.place(x=370,y=80)
   servicehour = Label(frame_emergency,text='Service Hour: 24Hour/7Days',font=('Times New Roman',20,),fg='black',bg='white')
   servicehour.place(x=350,y=140)

   frame_othernum = Frame(window_emergency,bg='white')
   frame_othernum.place(x=180,y=450,height=200,width=1000)

   title_othernum = Label(frame_othernum,text='Other Numbers\n\nCybersecurity:+603-88007999\nChild Abuse:15999\nRape:+603-21702200',font=('Times New Roman',20,'bold'),fg='black',bg='white')
   title_othernum.place(x=130,y=20)

   title_othercou = Label(frame_othernum,text='Other Country Numbers',font=('Times New Roman',20,'bold'),fg='black',bg='white')
   title_othercou.place(x=600,y=20)

   def other_counum():
       webbrowser.open('https://en.wikipedia.org/wiki/List_of_emergency_telephone_numbers')
   othercou_button=Button(frame_othernum,text='Link for other country',font=('Times New Roman',10),borderwidth=5,bg='white',fg='black',command=other_counum)
   othercou_button.place(x=650,y=80,height=50,width=200)

def discussion_page():
    window_dis = Tk()
    window_dis.title("Discussion Board")
    window_dis.geometry('800x800')
    window_dis.configure(bg='#ABB2B9')


    label_dis=Label(text='Discussion Board',font=('Times News Roman',20,'bold'),bg='#17202A',fg='white',)
    label_dis.place(x=0,y=20,height=70,width=800)
    #show message in text
    messages = Text(window_dis,bg='#17202A',font=('Times News Roman',15),fg='white')
    messages.place(x=60,y=110,height=560,width=680)
    

    # TextBox
    input_user = StringVar()
    input_message = Entry(window_dis,bg='#17202A',font=('Times News Roman',15),fg='white',text=input_user)
    input_message.place(x=60,y=700,height = 80,width =640)

    def printInput():
        input_get = input_message.get()
        print(input_get)
        messages.insert(INSERT,'You:''%s\n' % input_get)
        input_user.set('')
        return "break"

    input_message.bind("<Return>", printInput)
    
    # Button
    sendbutton = Button(window_dis,text = "Send",font=('Times News Roman',10,'bold'),bg='white',bd=5,command = printInput)
    sendbutton.place(x=710,y=715,height=50,width=65)

    scrollbar=ttk.Scrollbar(messages,orient='vertical',command=messages.yview)
    scrollbar.pack(side='right',fill='y')

    messages['yscrollcommand']=scrollbar.set

   
def user_login():
    user_email = text_email.get()
    user_password = text_password.get()
    if text_email.get()==''or text_password.get()=='':
       messagebox.showerror("Error","All Fields Are Required")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
            cursor=con.cursor()
            cursor.execute('Select * from users where Email_Address=%s and Password=%s',(text_email.get(),text_password.get()))
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Email Address & Password!")
            else:
                messagebox.showinfo(title='Welcome', message='Login Successful')
                main_page()
            con.close()
        except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}')
                
def register_page():
    def sign_up():
        signup_pass = signup_passwordentry.get()
        signup_passcomfirm = signup_confirmpasswordentry.get()
        if usernameentry.get()==""or signup_emailentry.get()==""or sec_signup_question.get()==""or signup_answerentry.get()==""or signup_passwordentry.get()==""or signup_confirmpasswordentry.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        elif signup_pass != signup_passcomfirm :
            messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif sec_signup_question.get()=="Select":
            messagebox.showerror('Error', 'Please choose the Security Questions')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
                cursor=con.cursor()
                cursor.execute('Select * from users where Email_Address=%s',signup_emailentry.get())
                row=cursor.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'Email Address already exist')
                else:
                     cursor.execute('insert into users(Username,Gender,Email_Address,Security_Questions,Answer,Password)values(%s,%s,%s,%s,%s,%s)',
                                   (usernameentry.get(),
                                    gendervalue.get(),
                                    signup_emailentry.get(),
                                    sec_signup_question.get(),
                                    signup_answerentry.get(),
                                    signup_passwordentry.get()
                                     ))
                     messagebox.showinfo(title='Welcome', message='You have successfully signed up!')
                con.commit()
                con.close()
            
                    

            except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}')
        window_reg.destroy()

    window_reg=Tk()
    window_reg.title('Registration Page')
    window_reg.geometry("1397x800")
    window_reg.configure(bg='#6c8ab0')

    #frame_for
    frame_reg = Frame(window_reg,bg='white')
    frame_reg.place(x=300,y=60,height=700,width=800)


    # Title
    title= Label(frame_reg,text="Registeration Form", font=("Times New Roman",35, 'bold'),fg='#3077cc',bg='white')
    title.place(x=180,y=10)

    #Field
    
    username = Label(frame_reg, text="Username:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
    signup_gender = Label(frame_reg, text="Gender:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
    signup_email = Label(frame_reg, text="Email address:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
    signup_question= Label(frame_reg,text='Security Question:',font=('Times New Roman',20,'bold'),fg='grey',bg='white')
    signup_answer= Label(frame_reg,text='Answer:',font=('Times New Roman',20,'bold'),fg='grey',bg='white')
    signup_password = Label(frame_reg, text="Password:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')
    signup_confirmpassword = Label(frame_reg, text="Confirm password:", font=("Times New Roman",20, 'bold'),fg='grey',bg='white')

    
    username.place(x=50,y=120)
    signup_gender.place(x=50,y=180)
    signup_email.place(x=50,y=240)
    signup_question.place(x=50,y=300)
    signup_answer.place(x=50,y=360)
    signup_password.place(x=50,y=420)
    signup_confirmpassword.place(x=50,y=480)
    
    usernamevalue = StringVar()
    signup_emailvalue = StringVar()
    gendervalue = IntVar()
    signup_questionvalue = StringVar()
    signup_answervalue = StringVar()
    signup_passwordvalue = StringVar()
    signup_confirmpasswordvalue = StringVar()
    
    

    
    usernameentry = Entry(frame_reg, textvariable =usernamevalue,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
    signup_emailentry = Entry(frame_reg, textvariable =signup_emailvalue,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
    #sec question
    ques=['Select','In what city were you born?','What is the name of your favorite pet?','What high school did you attend?','What is the name of your first school?',
          'What was the make of your first car?','What was your favorite food as a child?']
    sec_signup_question=ttk.Combobox(frame_reg,value=ques,font=('Times New Roman',15,'bold'))
    sec_signup_question.current(0)
    signup_answerentry = Entry(frame_reg,textvariable =signup_answervalue,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
    signup_passwordentry = Entry(frame_reg, textvariable =signup_passwordvalue,show='*',font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
    signup_confirmpasswordentry = Entry(frame_reg, textvariable =signup_confirmpasswordvalue,show='*',font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
    
    
    usernameentry.place(x=300,y=120,width=400,height=35)
    signup_emailentry.place(x=300,y=240,width=400,height=35)
    sec_signup_question.place(x=300,y=300,height=35,width=400)
    signup_answerentry.place(x=300,y=360,width=400,height=35)
    signup_passwordentry.place(x=300,y=420,width=400,height=35)
    signup_confirmpasswordentry.place(x=300,y=480,width=400,height=35)


    def show_hide1():
        if signup_passwordentry.cget('show') == '':
           signup_passwordentry.config(show='*')
           show_button1.config(text='show')
        else:
           signup_passwordentry.config(show='')
           show_button1.config(text='hide')
           

    def show_hide2():
        if signup_confirmpasswordentry.cget('show') == '':
           signup_confirmpasswordentry.config(show='*')
           show_button2.config(text='show')
        else:
           signup_confirmpasswordentry.config(show='')
           show_button2.config(text='hide')
           

    show_button1 = Button(frame_reg,text='show',borderwidth=5,bg='white',command=show_hide1)
    show_button1.place(x=700,y=420)
    
    show_button2 = Button(frame_reg,text='show',borderwidth=5,bg='white',command=show_hide2)
    show_button2.place(x=700,y=480)
    #Creating Checkbox
    agree=Label(frame_reg,text="Submit and Agree To The Terms & Conditions", font=("Times New Roman",10, 'bold'),bg='white').place(x=270,y=550,height=40,width=300)
    #Radio button
    Radiobutton(frame_reg, text="Male",font=("Times New Roman",15, 'bold'), variable=gendervalue, value=1,bg='white').place(x=300,y=180)
    Radiobutton(frame_reg, text="Female",font=("Times New Roman",15, 'bold'), variable=gendervalue, value=2,bg='white').place(x=400,y=180)

    #Submit button
    submitbtn = Button(frame_reg,text="Submit",font=("Times New Roman",20, 'bold'),borderwidth=10,bg='#3077cc',fg='white',command=sign_up)
    submitbtn.place(x=300,y=600,height=60,width=240)


         
def forgot_page():
    def forgot_password():
        if text_email.get()=='' or sec_question.get()==''or text_answer.get()==''or text_new_password.get()=='':
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
                cursor=con.cursor()
                cursor.execute('Select * from users where Email_Address=%s',text_email.get())
                row=cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid Email Address to reset your password")
                else:
                     con=pymysql.connect(host='localhost',user='root',password='',database='users_form')
                     cursor=con.cursor()
                     cursor.execute('Select * from users where Email_Address=%s and Security_Questions=%s and Answer=%s',(text_email.get(),sec_question.get(),text_answer.get()))
                     row1=cursor.fetchone()
                     if row1==None:
                        messagebox.showerror(title='Error', message='Please select correct Security Questions/Enter correct Answer!')
                     else:
                        cursor.execute('update users set Password=%s where Email_Address=%s',(text_new_password.get(),text_email.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success','Password has been reset')
                window_for.destroy()
            except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}')
            
        
    
    window_for = Tk()
    window_for.title('Forgot Password Page')
    window_for.geometry('1397x800')
    window_for.configure(bg='#6c8ab0')

    #frame_for
    frame_for = Frame(window_for,bg='white')
    frame_for.place(x=500,y=70,height=600,width=500)
    
    #title
    title = Label(frame_for,text='Forgot Password',font=('Times New Roman',35,'bold'),fg='#3077cc',bg='white')
    title.place(x=80,y=20)
 
    #email
    email = Label(frame_for,text='Email Address :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
    email.place(x=50,y=120)
 
    text_email = Entry(frame_for,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
    text_email.place(x=50,y=150,width=400,height=35)

    #sec question
    question= Label(frame_for,text='Security Question :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
    question.place(x=50,y=210)
    ques=['Select','In what city were you born?','What is the name of your favorite pet?','What high school did you attend?','What is the name of your first school?','What was the make of your first car?','What was your favorite food as a child?']
    sec_question=ttk.Combobox(frame_for,value=ques,font=('Times New Roman',15,'bold'))
    sec_question.current(0)
    sec_question.place(x=50,y=240,height=40,width=300)

    #answer
    answer= Label(frame_for,text='Answer :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
    answer.place(x=50,y=300)
  
    text_answer = Entry(frame_for,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf')
    text_answer.place(x=50,y=330,width=400,height=35)

    #password
    new_password = Label(frame_for,text='New Password :',font=('Times New Roman',15,'bold'),fg='grey',bg='white')
    new_password.place(x=50,y=390)
 
    text_new_password = Entry(frame_for,font=('Times New Roman',15,'bold'),fg='black',bg='#87a2bf',show='*')
    text_new_password.place(x=50,y=420,width=400,height=35)
    def show_hide():
        if text_new_password.cget('show') == '':
           text_new_password.config(show='*')
           show_button.config(text='show')
        else:
           text_new_password.config(show='')
           show_button.config(text='hide')
        
    #hide btn
    show_button = Button(frame_for,text='show',borderwidth=5,bg='white',command=show_hide)
    show_button.place(x=404,y=420) 
 
    
    #reset password button
    reset_password_button = Button(frame_for,text='RESET PASSWORD',font=('Times New Roman',15,'bold'),borderwidth=10,bg='#3077cc',fg='white',command=forgot_password)
    reset_password_button.place(x=130,y=500,height=60,width=240)



#login button
login_button = Button(frame_login,text='LOGIN',font=('Times New Roman',15,'bold'),borderwidth=10,bg='#3077cc',fg='white',command=user_login)
login_button.place(x=130,y=390,height=60,width=240)

#forget pass btn
forget_button = Button(frame_login,text='Forgot Password?',font=('Times New Roman',15,'bold','underline'),borderwidth=0,bg='white',fg='#3077cc',command=forgot_page)
forget_button.place(x=50,y=290)

def hide_eye():
    if text_password.cget('show') == '':
        text_password.config(show='*')
    else:
        text_password.config(show='')

#eye button
eye_image = PhotoImage(file='C:\\Users\\User\\OneDrive\\Pictures\\images\\show-password (1).png')
eye_image_label = Label(frame_login,image=eye_image,borderwidth=0)
eye_image_label.place(x=412,y=241)
eye_button = Button(frame_login,image=eye_image,borderwidth=0,bg='#87a2bf',command=hide_eye)
eye_button.place(x=412,y=241) 

#create an acc btn
acc_button = Button(frame_register,text='Create an account',font=('Times New Roman',15,'bold','underline'),borderwidth=0,bg='white',fg='#3077cc',command=register_page)
acc_button.place(x=220,y=33)
 
window.mainloop()
