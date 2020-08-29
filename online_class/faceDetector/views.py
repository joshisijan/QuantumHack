from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from imutils import paths
import numpy as np
import face_recognition
import pickle
import cv2
import os

from .forms import *
from .models import (
    UserFacesTraining,
    UserFaceRecognize,
    Attendence_class
)


def add_images(request):
    if request.method == "POST":
        form = AddFacesDataset(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../../face-recognition/add-images')
    else:
        form = AddFacesDataset()

    return render(request, 'add_images.html', {'form' : form})


def train_model(request):
    # if request.user.is_admin:
    if request.method == 'POST':
        file_location = str(settings.MEDIA_ROOT) + "/faceDetector/dataset"
        imagePaths = list(paths.list_images(file_location))
        knownEncodings = []
        knownNames = []

        for (i, imagePath) in enumerate(imagePaths):
            print('here...')
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
        dump_location = str(settings.MEDIA_ROOT) + "/faceDetector/encodings.pickle"
        f = open(dump_location, "wb")
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
def attendence_class(request, pk):
    if request.method == 'POST':
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        print('tesst...................')
        if(request.FILES['image']):
            selected_image = request.FILES['image']

            encoding_location = str(settings.MEDIA_ROOT) + "/faceDetector/encodings.pickle"
            data = pickle.loads(open(encoding_location, "rb").read())
            
            UserFaceRecognize.objects.create(
                user = request.user,
                image = selected_image
            ).save()

            image_location = str(settings.MEDIA_ROOT) + "/faceDetector/recognize/" + str(request.user.id) + '.png'
            print(image_location)
            print(image_location)
            print(image_location)
            print(image_location)
            print(image_location)
            image = cv2.imread(image_location)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # image = np.fromstring(selected_image, np.uint8)
            # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

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

            print(name)
            print(name)
            print(name)
            print(name)
            print(name)
            print(name)

            if(request.user.id == name):
                attendence = Attendence_exam.objects.filter(user=request.user, class_details=pk)
                if attendence:
                    return redirect(attendence.class_details.class_link)
                else:
                    Attendence_exam.objects.create(
                        user = request.user,
                        class_details = pk,
                        is_present = True,
                    )

            else:
                context = {
                    'message': "Face does't match"
                }
                return render(request, 'attendence_class.html', context)
        else:
            context = {
                    'message': "Sorry! We were not able to do recognization. Please try again."
                }
            return render(request, 'attendence_class.html', context)
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
                return redirect('redirection')
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
    return render(request, 'redirected.html')