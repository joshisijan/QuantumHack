from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings

from imutils import paths
import face_recognition
import pickle
import cv2
import os


def add_images(request):
    pass


def train_model(request):
    # if request.user.is_admin:
    if request.method == 'POST':
        imagePaths = list(paths.list_images(settings.MEDIA_ROOT + "/faceDetector/dataset"))
        knownEncodings = []
        knownNames = []

        for (i, imagePath) in enumerate(imagePaths):
            name = imagePath.split(os.path.sep)[-2]

            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            boxes = face_recognition.face_locations(rgb, model="cnn")    

            encodings = face_recognition.face_encodings(rgb, boxes)

            for encoding in encodings:
                knownEncodings.append(encoding)
                knownNames.append(name)

        data = {
            "encodings": knownEncodings,
            "names": knownNames
        }
        f = open(settings.MEDIA_ROOT + "/faceDetector/encodings.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()

        context = {
            'training': 'success'
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
    # else:
    #     return redirect('main_page')



# def attendence_class(request, classID):
def attendence_class(request):
    if request.method == 'POST':
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        if(request.FILES['image']):
            selected_image = request.Files['image']

            data = pickle.loads(open(settings.MEDIA_ROOT + "/faceDetector/encodings.pickle", "rb").read())
            image = cv2.imread(selected_image)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            boxes = face_recognition.face_locations(rgb, model="cnn")
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"], encoding)
                name = "Unknown"

                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    name = max(counts, key=counts.get)

                names.append(name)

            if(request.user.id == name):
                return redirect('redirection')
            else:
                context = {
                    'message': "Face does't match"
                }
                return render(request, 'attendence_class.html', context)
        else:
            context = {
                    'message': "Sorry! We were not able to do recognization. Please try again."
                }
            return render(request, 'home.html', context)
    else:
        print('no........')
        print('no........')
        print('no........')
        print('no........')
        print('no........')
        return render(request, 'attendence_class.html')




def attendence_exam(request, examId):
    if request.method == 'POST':
        if(request.FILES['image']):
            selected_image = request.Files['image']

            data = pickle.loads(open(settings.MEDIA_ROOT + "/faceDetector/encodings.pickle", "rb").read())
            image = cv2.imread(selected_image)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            boxes = face_recognition.face_locations(rgb, model="cnn")
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"], encoding)
                name = "Unknown"

                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    name = max(counts, key=counts.get)

                names.append(name)

            if(request.user.id == name):
                return redirect('assignment_page')
            else:
                context = {
                    'message': "Face does't match"
                }
                return render(request, 'attendence-class.html', context)
        else:
            context = {
                    'message': "Sorry! We were not able to do recognization. Please try again."
                }
            return render(request, 'attendence-class.html', context)
    else:
        return render(request, 'attendence-class.html')

def redirection(request):
    pass