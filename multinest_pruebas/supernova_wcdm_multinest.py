import json
import numpy as np
import scipy.stats
import scipy
import pymultinest
import matplotlib.pyplot as plt
import pandas as pd

from astropy.cosmology import wCDM
import astropy.units as u


def prior(cube, ndim, nparams):
    cube[0] = cube[0] * 4
    cube[1] = cube[1] * 8
    cube[2] = cube[2] * 40 + 50
    cube[3] = cube[3] * 0.7
    cube[4] = cube[4]
    cube[5] = cube[5] * 2.0 - 2.0 


def loglike(cube, ndim, nparams):

    alpha = cube[0]
    beta = cube[1]
    H0 = cube[2]
    Om = cube[3]
    Ol = cube[4]
    w0 = cube[5]

    cosmo = wCDM(H0=H0, Om0=Om, Ode0=Ol, w0=w0)

    model = 5 * np.log10(
        cosmo.luminosity_distance(z).to(u.pc).value / 10
    )

    data_model = mB + alpha * x1 - beta * c + 19.252

    dD = data_model - model

    logL = -0.5 * (dD @ C_inv @ dD)

    return logL


data = pd.read_csv(
    '/Users/juda/lab_alma/Pantheon+SH0ES.dat',
    sep=' '
)

err = np.genfromtxt(
    "/Users/juda/lab_alma/Pantheon+SH0ES_STATONLY.cov",
    delimiter=" ",
    usemask=False,
    skip_header=1
)

# Dividimos los datos
z = np.array(data['zHD'])
mB = np.array(data['mB'])
c = np.array(data['c'])
x1 = np.array(data['x1'])

# Matriz de covarianza
C_stat = np.reshape(err, (1701, 1701))

# Inversa
C_inv = np.linalg.inv(C_stat)

# Parámetros
parameters = ['alpha', 'beta', 'H0', 'Om', 'Ol', 'w0']
n_params = len(parameters)

# Ejecutar MultiNest
pymultinest.run(
    loglike,
    prior,
    n_params,
    outputfiles_basename='/Users/juda/lab_alma/multinest_pruebas/chain_supernova_wcdm/',
    resume=False,
    verbose=True,
    n_live_points=2000
)

json.dump(
    parameters,
    open(
        '/Users/juda/lab_alma/multinest_pruebas/chain_supernova_lcdm/params.json',
        'w'
    )
)