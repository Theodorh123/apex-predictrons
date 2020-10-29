from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import date
from phone_field import PhoneField
from django.contrib.auth import get_user_model
from django.contrib import messages
# importing tensorflow libs needed
from tensorflow import keras
from keras.preprocessing import image
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model, model_from_json
from keras.initializers import glorot_uniform
from keras.utils import CustomObjectScope
from keras.optimizers import Adam
from keras import backend as K
from keras.losses import categorical_crossentropy
from keras.applications.mobilenet import preprocess_input
# importing numpy
import numpy as np
# import the reverse url
from django.urls import reverse

# get custom user
User = get_user_model()


class Prediction(models.Model):
    
    physician = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(_("Patient\'s name"), max_length=500, null=False, blank=False)
    xray_image = models.ImageField(_("X-ray image"), upload_to=None, height_field=None, width_field=None, max_length=None)
    classification_result = models.CharField(_("Prediction result"), max_length=500)
    
    def __str__(self):
        return self.patient_name

    def make_prediction(self):
        K.reset_uids()
        model = ""
        weights = ""
        classes = {
            'TRAIN': ['GRADE 0', 'GRADE 1', 'GRADE 2', 'GRADE 3', 'GRADE 4'],
            'VALIDATION': ['GRADE 0', 'GRADE 1', 'GRADE 2', 'GRADE 3', 'GRADE 4'],
            'TEST': ['GRADE 0', 'GRADE 1', 'GRADE 2', 'GRADE 3', 'GRADE 4'],
        }    
        
        with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
            with open(model, 'r') as f:
                model = model_from_json(f.read())
                model.load_weights(weights)

        xray_image = image.load_img(self.img, target_size=(224, 224))
        x = image.img_to_array(xray_image)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        model.compile(loss="categorical_crossentropy", metrics=[
                      "accuracy"], optimizer="adam")
        result = model.predict(x)

        pred_name = classes['TRAIN'][np.argmax(result)]

        messages.success(result, f"The osteoarthritis is predicted to be {pred_name}".format(pred_name))

        return pred_name
              

    # save the prediction result from the make prediction method
    def save(self, *args, **kwargs):
        self.classification_result = self.make_prediction()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
        