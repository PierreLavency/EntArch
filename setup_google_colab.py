import os

def download_github_code(path):
    filename = path.rsplit("/")[-1]
    os.system("shred -u {}".format(filename))
    course = 'bayesian-methods-for-ml'
    branch = 'master'
    url = 'https://raw.githubusercontent.com/hse-aml/{}/{}/{}'
    template = "wget '" + url + "' -O '{}'"
    os.system(template.format(course, branch, path, filename))


def download_github_lfs(path):
    filename = path.rsplit("/")[-1]
    os.system("shred -u {}".format(filename))
    course = 'bayesian-methods-for-ml'
    branch = 'master'
    url = "https://github.com/hse-aml/{}/blob/{}/{}?raw=true"
    template = "wget '" + url + "' -O '{}'"
    os.system(template.format(course, branch, path, filename))


def load_data_week2():
    download_github_code("week2/w2_grader.py")
    download_github_code("week2/samples.npz")

def load_data_final_project():
    download_github_code("week7_(final_project)/utils.py")
    download_github_lfs("week7_(final_project)/CelebA_VAE_small_8.h5")