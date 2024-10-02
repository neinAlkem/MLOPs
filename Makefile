DATA_DIR = data/pre_processing
RAW_DIR = data/raw
MODEL_DIR = models
SCRIPTS_DIR = scripts
RESULT_DIR = result
CONDA_ENV = myenv
all: create_env activate_env install_deps data train evaluate deploy

create_env:
	cmd /c call environment.bat

activate_env:
	cmd /c call activate_env.bat

install_deps:
	@echo "Mengunduh dependencies.."
	conda run -n $(CONDA_ENV) pip install -r requirements.txt

data: install_deps
	@echo "Proses Pengunduhan dan Pre-Processing Data.."
	conda run -n $(CONDA_ENV) python $(SCRIPTS_DIR)/data_prep.py 

train: data
	@echo "Proses Pelatihan Model dengan Data Latih.."
	conda run -n $(CONDA_ENV) python $(SCRIPTS_DIR)/train_model.py

evaluate: train
	@echo "Proses Evaluasi terhadap Model dengan Menggunakan Data Uji.."
	conda run -n $(CONDA_ENV) python $(SCRIPTS_DIR)/evaluate_model.py

deploy: evaluate
	@echo "Menyimpan model terlatih.."
	conda run -n $(CONDA_ENV) python $(SCRIPTS_DIR)/deploy_model.py

clean:
	@echo "Membersihkan file hasil sebelumnya.."
	rm -rf $(DATA_DIR)/*
	rm -rf $(MODEL_DIR)/*
	rm -rf $(RESULT_DIR)/*
	rm -rf $(RAW_DIR)/*
	conda remove --name $(CONDA_ENV) --all -y

