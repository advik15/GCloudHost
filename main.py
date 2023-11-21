from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import contractions
from flask import Flask,jsonify


app = Flask(__name__)


@app.route("/")
def hello() -> str:


    #document0 = input("Enter emails: ")
    document0 = "testing on advik sachdeva"
    document1 = 'Subject: Meeting Request for Project Kickoff Dear [Recipient\'s Name], I hope this email finds you well. I would like to request a meeting to discuss the upcoming project kickoff. Our team has made significant progress in the planning phase, and it is crucial that we align on the next steps and assign responsibilities. Are you available for a meeting on [Proposed Date and Time]? Please let me know your availability, and I will send out a calendar invite. Best regards,[Your Name]'
    document2 = 'Subject: Project Status Update - Milestone Achieved Dear [Recipient\'s Name], I wanted to inform you that we have successfully achieved a major milestone in our project. Our team worked diligently to meet the deadline, and I am pleased to share the details in the attached report. Please review the document and let me know if you have any questions or require further information. Regards, [Your Name]'
    document3 = 'Subject: Job Offer for [Position] Dear [Candidate\'s Name], We are delighted to extend an offer for the [Position] role at [Company Name]. We were thoroughly impressed with your qualifications and believe you will be a valuable addition to our team. Please find the attached offer letter with details about compensation, benefits, and other important information. We look forward to your positive response. Best regards, [Your Name]'
    document4 = 'Subject: Resignation Letter Dear [Supervisor\'s Name], I am writing to formally resign from my position as [Your Position] at [Company Name]. It has been an incredible journey working with the team, but I have decided to explore new opportunities. I am committed to ensuring a smooth transition. Please let me know how I can be of assistance during this period. Sincerely, [Your Name]'
    document5 = 'Subject: Follow-Up on Interview Dear [Interviewer\'s Name], I wanted to express my gratitude for the opportunity to interview for the [Position] role at [Company Name]. I am eager to contribute to the team and believe my skills align with the job requirements. If there are any additional steps or information needed from my end, please don\'t hesitate to reach out. Best regards, [Your Name]'
    document6 = 'Subject: Information Request for [Project/Task] Dear [Recipient\'s Name], I am currently working on [Project/Task] and require some specific information to move forward. Could you please provide the following details: [List of information needed]? Your assistance in this matter is greatly appreciated. Regards, [Your Name]'
    document7 = 'Subject: Request for Promotion Consideration Dear [Supervisor\'s Name], I have thoroughly enjoyed my time at [Company Name] and have consistently contributed to our teams success. I would like to formally request consideration for a promotion to [Desired Position] based on my achievements and the value I believe I can bring to the organization in this new role. I am open to discussing this further at your convenience. Sincerely, [Your Name]'
    document8 = 'Subject: Formal Complaint Dear [HR Manager\'s Name], I am writing to formally submit a complaint regarding [Describe the issue]. I believe it is essential to address this matter to maintain a healthy work environment. I am available to discuss this issue further with HR or any relevant parties. Thank you, [Your Name]'
    document9 = 'Subject: Follow-Up on Recent Meeting Dear [Client\'s Name], I hope this message finds you well. I wanted to follow up on our recent meeting and discuss the action items and next steps. Please let me know your availability for a follow-up call. Best regards, [Your Name]'
    document10 = 'Subject: New Hire Announcement Dear [Company Name] Team, We are delighted to announce that [New Employee\'s Name] has joined our team as [Position]. [Brief introduction of the new hire].Please join us in welcoming [New Employees Name] to the [Company Name] family. Best regards, [Your Name]'
    document11 = 'Subject: Congratulations on Achieving [Milestone] Dear [Colleague\'s Name], I wanted to extend my warmest congratulations on the successful achievement of [Milestone]. Your hard work and dedication have been instrumental in reaching this significant milestone. Well done! Best wishes, [Your Name]'
    document12 = 'Subject: Feedback on Your Presentation Dear [Presenter\'s Name], I attended your recent presentation on [Topic], and I wanted to provide some feedback. Overall, it was informative and engaging. However, I believe there could be room for improvement in [Specific Aspect of the Presentation]. I appreciate your efforts and look forward to your continued success in future presentations. Sincerely, [Your Name]'
    document13 = 'Subject: Request for Project Deadline Extension Dear [Project Manager\'s Name], I regret to inform you that our team is facing unexpected challenges that may affect our ability to meet the current project deadline. I\'m kindly requesting an extension to ensure the quality and success of the project.I am willing to discuss this further and provide additional information as needed. Best regards, [Your Name]'
    document14 = 'Subject: Request for Letter of Recommendation Dear [Colleague\'s Name], I hope this message finds you well. I am currently applying for [Opportunity], and I am in need of a letter of recommendation. I believe your insights and experience working with me would greatly benefit my application. Please let me know if you are willing to provide a recommendation, and I will provide any necessary details. Thank you for considering my request. Sincerely, [Your Name]'
    document15 = 'Subject: Submission of Proposal for [Client\'s Project] Dear [Client\'s Name], I am pleased to submit our proposal for [Client\'s Project]. Our team has carefully reviewed the project requirements, and we believe our proposal offers a comprehensive solution that aligns with your goals. Please find the attached proposal document, and I am available for any further discussions or clarifications. Best regards, [Your Name]'
    document16 = 'Subject: Project Update - [Project Name] Dear [Stakeholders\' Names], I wanted to provide a comprehensive update on the progress of [Project Name]. We have made significant strides, and I believe it\'s essential to share the details of our achievements and upcoming milestones. Please find the attached project update report for your review. Best regards, [Your Name]'
    document17 = 'Subject: Delegation of [Task] - [Recipient\'s Name] Dear [Recipient\'s Name], I hope you\'re doing well. I would like to delegate the task of [Task] to you as I believe your skills and expertise are well-suited for this responsibility. Please find the details and guidelines attached, and let\'s schedule a brief discussion to ensure clarity. Thank you for your assistance. Regards, [Your Name]'
    document18 = 'Subject: Reminder - [Training Name] on [Date] Dear [Employee\'s Name], This is a friendly reminder about the upcoming training session, [Training Name], scheduled for [Date] at [Location]. We believe that this training will be highly beneficial for your professional development and the growth of our team. Please ensure that you have made the necessary arrangements to attend. If you have any questions or require additional information, don\'t hesitate to reach out. We look forward to your active participation. Regards, [Your Name]'
    document19 = 'Subject: Request for Performance Review Meeting Dear [Supervisor\'s Name], As part of my professional growth and development, I would like to request a performance review meeting to discuss my progress, goals, and areas of improvement. I believe that your feedback and insights will be valuable for my career advancement. Please let me know your availability, and I will be prepared for the discussion. Thank you for your support. Sincerely, [Your Name]'
    document20 = 'Subject: Sick Leave Notification - [Your Name] Dear [Supervisor\'s Name], I\'m writing to inform you that I am unwell and unable to come to work due to [Explain the reason]. I have attached my medical certificate for your reference. I anticipate being on sick leave from [Start Date] to [End Date]. Please let me know if there are any specific procedures or tasks I should follow during my absence. Thank you for your understanding. Best regards, [Your Name]'
    document21 = 'Subject: Request for Budget Approval - [Project Name] Dear [Budget Approver\'s Name], I am writing to request your approval for the budget proposal related to the [Project Name]. This budget is essential for the successful execution of the project and aligns with our project goals. Please review the attached budget proposal and let me know if you have any questions or require further information. Your timely approval is crucial to keep the project on schedule. Thank you for your consideration. Regards, [Your Name]'
    document22 = 'Subject: Join Us for a Team Building Event! Hey Team, We\'re excited to announce a team-building event on [Date] at [Location]. It\'s a fantastic opportunity to strengthen our bonds, enhance collaboration, and have some fun together. Please RSVP by [RSVP Deadline] so we can make the necessary arrangements. We look forward to an amazing event! Cheers, [Your Name]'
    document23 = 'Subject: [Meeting Date] Meeting Recap and Action Items Dear [Meeting Attendees\' Names], I hope you had a chance to review the meeting minutes from our [Meeting Date] meeting. The document contains a summary of our discussions, decisions, and assigned action items. If you have any updates or clarifications to provide, please reply to this email. Let\'s ensure we\'re all on the same page as we move forward with our tasks. Thank you for your engagement during the meeting. Regards, [Your Name]'
    document24 = 'Subject: New Employee Orientation Information Dear [New Employee\'s Name], Welcome to the [Company Name] team! We\'re excited to have you on board. Your orientation is scheduled for [Orientation Date] at [Orientation Location]. Attached is an agenda for the day, which includes an introduction to our company, policies, and a tour of the facilities. Please let us know if you have any specific questions or requirements. We look forward to your first day with us. Best regards, [Your Name]'
    document25 = 'Subject: Change in [Project Name] Timeline Dear [Project Team/Stakeholders], I\'m writing to inform you of a change in the timeline for our [Project Name]. Due to unforeseen circumstances, we need to adjust our project schedule. Please find the attached document outlining the revised timeline and the reasons behind this change. If you have any questions or concerns, please reach out for further clarification. Your flexibility and understanding are greatly appreciated. Regards, [Your Name]'
    document26 = 'Subject: Resolution of [Conflict Issue] Dear [Colleague\'s Name], I\'m writing to inform you that we have successfully resolved the recent conflict regarding [Conflict Issue]. We appreciate your patience and constructive approach in reaching a resolution. If you have any concerns or additional feedback, please do not hesitate to communicate. Thank you for your professionalism in addressing this matter. Sincerely, [Your Name]'
    document27 = 'Subject: Request for Training Budget Approval Dear [Manager\'s Name], I am seeking approval for the training budget necessary to attend the [Training Name] scheduled for [Training Dates]. This training is directly aligned with my professional development goals and will benefit our team. Please find attached the training details and budget proposal for your review. Your approval will greatly assist in my ongoing growth and contributions to the team. Thank you for considering my request. Regards, [Your Name]'
    document28 = 'Subject: Promotion Announcement - [Employee\'s Name] Dear Team, We are thrilled to announce the promotion of [Employee\'s Name] to the position of [New Position Title]. [Employee\'s Name] has consistently demonstrated dedication, exceptional skills, and leadership within our organization. We are confident that [Employee\'s Name] will excel in this new role and contribute to our continued success. Please join us in congratulating [Employee\'s Name] on this well-deserved promotion. Best regards, [Your Name]'
    document29 = 'Subject: We Value Your Feedback Dear Team, Your insights and feedback are essential to our organization\'s growth and development. We are conducting an employee survey to gain a better understanding of your experiences and suggestions for improvement. Please take a few moments to complete the survey linked here [Survey Link]. Your responses will remain confidential, and your input will help shape our future initiatives. Thank you for your participation. Regards, [Your Name]'
    document30 = 'Subject: Request for a Meeting Hi [Colleague\'s Name], I hope this email finds you well. I\'d like to request a meeting to discuss [Topic/Agenda]. Your insights and expertise in this area would be invaluable. Are you available on [Proposed Date and Time]? Please let me know your availability, and I\'ll schedule the meeting accordingly. Looking forward to our discussion. Regards, [Your Name]'


    documentList = [document0, document1, document2, document3, document4, document5, document6, document7, document8, document9, document10, 
                    document11, document12, document13, document14, document15, document16, document17, document18, document19, document20,
                    document21, document22, document23, document24, document25, document26, document27, document28, document29, document30]

    for i in range(len(documentList)):
        documentList[i] = contractions.fix(documentList[i])

    tfidf = TfidfVectorizer(analyzer='word', stop_words= 'english')
    result = tfidf.fit_transform(documentList)
    tokens = tfidf.get_feature_names_out()

    df_tfidf = pd.DataFrame(data = result.toarray(),index = ['Doc0','Doc1','Doc2','Doc3','Doc4','Doc5','Doc6','Doc7','Doc8','Doc9','Doc10',
                                                            'Doc11','Doc12','Doc13','Doc14','Doc15','Doc16','Doc17','Doc18','Doc19','Doc20',
                                                            'Doc21','Doc22', 'Doc23','Doc24','Doc25','Doc26','Doc27','Doc28','Doc29','Doc30'] ,columns = tokens)
    df_tfidf.drop(df_tfidf.index[1:31], inplace=True)
    df_tfidf = df_tfidf.transpose()
    df_tfidf = df_tfidf[df_tfidf['Doc0'] > 0.0]
    df_tfidf = df_tfidf.sort_values(by = 'Doc0', ascending = False)
    df_tfidf = df_tfidf.head(15)

   
    response = jsonify(df_tfidf.to_dict())
    response.status_code = 200  # You can set the status code that you prefer
    return response



if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_flex_quickstart]
