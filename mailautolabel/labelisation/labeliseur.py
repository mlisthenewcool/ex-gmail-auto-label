import ml.supervised
import csv_helper
from  graphics.interface_graphique import affiche
import sys

#######################################################################
#                Ajout d'un label a un mail                           #
#######################################################################
def ajoutLabel(service,labelId,messageId):
	"""
	Ajoute le label "labelId" au mail "messageId"
	"""
	userId = "me"
	body = {'addLabelIds': [labelId]}
   
	results_m = service.users().messages().list(userId='me').execute()
	results = service.users().messages().modify(userId=userId, id=messageId, body=body).execute()

def gmailLabelisation(service,username,label =None,fenetre = None):
	affiche("--------------------------------------\n",0,label ,fenetre)
	affiche("MACHINE LEARNING\n",1,label,fenetre)
	mails_nonlab = csv_helper.toDict("NON_LABEL"+username)

	prediction = ml.supervised.supervisedWithNolabellingMail(username)
	if(prediction == "NON_LABEL VIDE"):
		affiche("Tous vos mails possèdent déjà un label ! \nAttendez d'avoir de nouveaux mails à labéliser.\n",0,label ,fenetre)
	elif(prediction == "LABEL VIDE"):
		affiche("Votre boite mail ne contient aucun mail labélisé!\nTrier une première fois votre boite mail pour\n que la labélisation automatique soit possible\n",0,label ,fenetre)
	else:
		affiche("--------------------------------------\n",1,label,fenetre)
		affiche("Labélisation des mails en cours\n",1,label,fenetre)
		for i in range(len(prediction)):
			affiche(str(i)+"/"+str(len(prediction)-1)+"\n" ,1,label,fenetre)
			ajoutLabel(service = service,labelId = prediction[i],messageId = mails_nonlab[i]['id'])
