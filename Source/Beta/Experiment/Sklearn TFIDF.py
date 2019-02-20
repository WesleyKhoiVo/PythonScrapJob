# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 10:28:31 2019

@author: khoim
"""


from sklearn.feature_extraction.text import TfidfVectorizer

docA = "What impact will you make?At Deloitte, we offer a unique and exceptional career experience to inspire and empower talents like you to make an impact that matters for our clients, people and society. Whatever your aspirations, Deloitte offers you unrivalled opportunities to realise your full potential. We are always looking for people with the relentless energy to push themselves further, and to find new avenues and unique ways to reach our shared goals. So what are you waiting for? Join the winning team now.Work you’ll do: Can you think both analytically and creatively? Then this is where you’ll thrive. We’re more involved in our clients’ affairs than ever before, providing advice and services far beyond pure financial diligence. Whether it is business restructuring, mergers and acquisitions, investments or business model generations, you’ll gain exposure to a huge variety of projects and a diverse portfolio of clients. All whilst finding the cleverest solutions to the most complex problems.Responsibilities: Gathering and synthesising financial and operating information about companies, industries and governments.Gathering market data to analyse trends.Drafting presentations for internal audience within the Firm and external clients.Attending team discussions and client meetings.Requirements: Background in accounting, auditing, economics, commerce, finance, banking, law, foreign trade.Strong analytical and numerical skills.Excellent command of English, both verbal and written.Ethical behaviour.Strong interpersonal and team working skills.Enthusiasm and ability to assume a high level of responsibilities.High commitment to succeed and continue learning.Strong record of academic achievement as per latest GPA score.Application processCandidates access Deloitte Career website and create account for online application.Upload the below required documents: The most updated resume with profile picture.The most updated certified transcript/degree.Due to volume of applications, we regret only shortlisted candidates will be notified. In Vietnam, the services are provided by Deloitte Vietnam Company Limited and other related entities in Vietnam ("Deloitte in Vietnam"), which are affiliates of Deloitte Southeast Asia Ltd. Deloitte Southeast Asia Ltd is a member firm of Deloitte Touche Tohmatsu Limited. Deloitte in Vietnam, which is within the Deloitte Network, is the entity that is providing this Website."
docB = "The truck is driven on the highway"

tfidf = TfidfVectorizer()

response = tfidf.fit_transform([docA, docB])


feature_names = tfidf.get_feature_names()
for col in response.nonzero()[1]:
    print (feature_names[col], ' - ', response[0, col])
    
