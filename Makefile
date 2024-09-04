DATA_DIR = data
MODEL_DIR = models
SCRIPTS_DIR = scripts
RESULT_DIR = result

all: data train evaluate deploy

data:
	@echo "Mengunduh dan memproses data..."
	python $(SCRIPTS_DIR)/data_prep.py

train: data
	@echo "Melatih model..."
	python $(SCRIPTS_DIR)/train_model.py

evaluate: train
	@echo "Mengevaluasi model..."
	python $(SCRIPTS_DIR)/evaluate_model.py

deploy: evaluate
	@echo "Menyimpan model terlatih..."
	python $(SCRIPTS_DIR)/deploy_model.py

clean:
	@echo "Membersihkan file sementara..."
	rm -rf $(DATA_DIR)/*
	rm -rf $(MODEL_DIR)/*
	rm -rf $(RESULT_DIR)/*
