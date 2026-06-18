from getdist import loadMCSamples, plots

samples = loadMCSamples('/Users/juda/lab_alma/proyecto_final/chains/proyecto_only_desibao/proyecto_only_desibao')

g = plots.get_subplot_plotter()
g.triangle_plot(samples, ['H0', 'omega_b', 'omega_cdm'], filled=True)
g.export('triangle_plot_only_desibao.png')
