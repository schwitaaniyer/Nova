from flask import Flask, render_template,request
import quantum as q

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/quantum')
def quantum():
    return render_template('quantum.html')

@app.route('/quantum/bohr_model',methods = ['GET','POST'])
def bohr_model():
    if request.method == 'POST':
        E1 = float(request.form.get('one'))
        E2 = float(request.form.get('two'))
        bohr_model = q.bohr_model(E1,E2)
        return '<br><br><br><br><br><br><br><br><center><h1>Bohr Model is: '+str(bohr_model)+'kg metre sec^-1'+'</h1></center>'
        
    return render_template('quantum_bohr.html')

@app.route('/quantum/compton_scattering',methods = ['GET','POST'])
def compton_scattering():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        theta = float(request.form.get('two'))
        c_scattering = q.compton_scattering(m,theta)
        return '<br><br><br><br><br><br><br><br><center><h1>Compton Scattering is: '+str(c_scattering)+' metre/sec'+'</h1></center>'
        
    return render_template('quantum_c_scattering.html')

@app.route('/quantum/compton_wavelength',methods = ['GET','POST'])
def compton_wavelength():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        c_wavelength = q.compton_wavelength(m)
        return '<br><br><br><br><br><br><br><br><center><h1>Compton Wavelength is: '+str(c_wavelength)+' metre sec^2'+'</h1></center>'
        
    return render_template('quantum_c_wavelength.html')

@app.route('/quantum/curie_constant',methods = ['GET','POST'])
def curie_constant():
    if request.method == 'POST':
        N = float(request.form.get('one'))
        a = float(request.form.get('two'))
        u = float(request.form.get('three'))
        cu_con = q.curie_constant(N,a,u)
        return '<br><br><br><br><br><br><br><br><center><h1>Curie Constant is: '+str(cu_con)+' metre sec^2'+'</h1></center>'
        
    return render_template('quantum_cu_con.html')

@app.route('/quantum/de_broglie_wavelength',methods = ['GET','POST'])
def de_broglie_wavelength():
    if request.method == 'POST':
        m = float(request.form.get('one'))
        v = float(request.form.get('two'))
        p = float(request.form.get('three'))
        de_broglie = q.de_broglie_wavelength(m,v,p)
        return '<br><br><br><br><br><br><br><br><center><h1>de Broglie Wavelength is: '+str(de_broglie)+' metre sec^2'+'</h1></center>'
        
    return render_template('quantum_de_broglie.html')

@app.route('/quantum/hydrogen_energy',methods = ['GET','POST'])
def hydrogen_energy():
    if request.method == 'POST':
        n = float(request.form.get('one'))
        z = float(request.form.get('two'))
        hy_en = q.hydrogen_energy(n,z)
        return '<br><br><br><br><br><br><br><br><center><h1>Hydrogen Energy is: '+str(hy_en)+' Joule'+'</h1></center>'
        
    return render_template('quantum_hy_en.html')

@app.route('/quantum/photoelectric_effect',methods = ['GET','POST'])
def photoelectric_effect():
    if request.method == 'POST':
        f = float(request.form.get('one'))
        f0 = float(request.form.get('two'))
        PE = q.photoelectric_effect(f,f0)
        return '<br><br><br><br><br><br><br><br><center><h1>Photoelectric Effect is: '+str(PE)+' Joule'+'</h1></center>'
        
    return render_template('quantum_PE.html')

@app.route('/quantum/photon_energy',methods = ['GET','POST'])
def photon_energy():
    if request.method == 'POST':
        w = float(request.form.get('one'))
        ph_en = q.photon_energy(w)
        return '<br><br><br><br><br><br><br><br><center><h1>Photon Energy is: '+str(ph_en)+' Joule'+'</h1></center>'
        
    return render_template('quantum_ph_en.html')

@app.route('/quantum/rydberg_eqn',methods = ['GET','POST'])
def rydberg_eqn():
    if request.method == 'POST':
        z = float(request.form.get('one'))
        n1 = float(request.form.get('two'))
        n2 = float(request.form.get('three'))
        ry_eqn = q.rydberg_eqn(z,n1,n2)
        return '<br><br><br><br><br><br><br><br><center><h1>Rydberg Equation is: '+str(ry_eqn)+' Watt'+'</h1></center>'
        
    return render_template('quantum_ry_eqn.html')

@app.route('/quantum/stefan_boltzmann',methods = ['GET','POST'])
def stefan_boltzmann():
    if request.method == 'POST':
        a = float(request.form.get('one'))
        t = float(request.form.get('two'))
        e = float(request.form.get('three'))
        st_bo = q.stefan_boltzmann(a,t,e)
        return '<br><br><br><br><br><br><br><br><center><h1>Stefan Boltzmann Constant is: '+str(st_bo)+' Kg metre^2'+'</h1></center>'
        
    return render_template('quantum_ste_boltz.html')

@app.route('/quantum/wein_law_pw',methods = ['GET','POST'])
def wein_law_pw():
    if request.method == 'POST':
        bbt = float(request.form.get('one'))
        pw = q.wein_law_pw(bbt)
        return '<br><br><br><br><br><br><br><br><center><h1>Peak Wavelength is: '+str(pw)+' Kg metre^2'+'</h1></center>'
        
    return render_template('quantum_wein_pw.html')

@app.route('/quantum/wein_law_pf',methods = ['GET','POST'])
def wein_law_pf():
    if request.method == 'POST':
        bbt = float(request.form.get('one'))
        pf = q.wein_law_pf(bbt)
        return '<br><br><br><br><br><br><br><br><center><h1>Peak Frequency is: '+str(pf)+' Metre'+'</h1></center>'
        
    return render_template('quantum_wein_pf.html')

if __name__ == '__main__':
    app.run(debug = True)