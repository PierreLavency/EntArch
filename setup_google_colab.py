import os

def download_github_code(path):
    filename = path.rsplit("/")[-1]
    os.system("shred -u {}".format(filename))
    rep = 'EntArch'
    branch = 'master'
    url = 'https://raw.githubusercontent.com/PierreLavency/{}/{}/{}'
    template = "wget '" + url + "' -O '{}'"
    os.system(template.format(rep, branch, path, filename))

def download_github_lfs(path):
    filename = path.rsplit("/")[-1]
    os.system("shred -u {}".format(filename))
    rep = 'EntArch'
    branch = 'master'
    url = "https://github.com/PierreLavency/{}/blob/{}/{}?raw=true"
    template = "wget '" + url + "' -O '{}'"
    os.system(template.format(rep, branch, path, filename))

def load_data(dim=26) :
    path="/Data/CBL_"+str(dim)+"_features.csv"
    download_github_code(path)
        
def load_data_final_project():
    download_github_code("week7_(final_project)/utils.py")
    download_github_lfs("week7_(final_project)/CelebA_VAE_small_8.h5")