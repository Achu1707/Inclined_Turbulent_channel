require 'seeder'
require 'musubi'

print('##Physical parameters##')
print('MachNr =',Ma)
print('Re_tau =', Re_tau)
print('u_fric_p =', vel_fric_phy)
print('Re_bulk =', Re_bulk)
print('u_bulk_p =', vel_bulk_phy)
--print('u_bulk_dns_p =', vel_bulk_dns_phy)
print('nu_p =', nu_phy)
print('rho0_p =', rho_phy)
print('p0_p =', press_ambient)
print('cs_p =', cs_phy)
print('force =', accel)
print('T_c=', T_c)
print('L_c=', delta_nu)
print('y_plus=', dx/2.0*vel_fric_phy/nu_phy)
print('length =', length)
print('height =', height)
print('width=',width)
print('dx =',dx)
print('dt =',dt)
print('level =', level)
print('')
print('##e parameters##')
print('nLength =', nLength)
print('nHeight =', nHeight)
print('u_bulk_L =', vel_bulk_L)
print('u_fric_L =', vel_fric_phy*dt/dx)
print('nu_L =', nu_L)
print('omega =', omega)
