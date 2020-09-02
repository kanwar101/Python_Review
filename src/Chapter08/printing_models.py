unverified_models = ['Nokia','Moto','Apple','Android']
verified_models = []

def printing_models(unverified_models, verified_models):
	"""Printing models after copying to empty list"""

	while unverified_models:
		current_model = unverified_models.pop()
		print (current_model)
		verified_models.append(current_model)

print (unverified_models)
def show_models_completed (verified_models):
	for model in verified_models:
		print (model)


printing_models (unverified_models[:], verified_models)
show_models_completed(verified_models)

print(unverified_models)

