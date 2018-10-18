def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

c = 4029014245677043546027611173458745791308707741524806603125715399519387859880456525253046869331145070296742183163437034345629735710862401584332627503167608495279106827037943756648675621534144189803641767093636912981051013939143169305795500214328030691929103692765169254133610765720044368542590591435860
n = 6154808998720852688941597559268958678420017083063528542562488199931785619480350784637047275430179382424289423795573619385102587648834298373661020219228088139255029194748861701920718722877508948446241081323888058945640955064368098993956157190646174853988842763577299679331265041873146486532360869088707563
e = 65537

primes = [
          3070268809,
          4073110357,
          2893223539,
          3621797999,
          4114621897,
          3082112711,
          4251183767,
          2785701817,
          2241458839,
          3736695979,
          2747195677,
          4018065301,
          3387127147,
          2348661407,
          2402005841,
          3266912417,
          2225970311,
          3245512111,
          3090248153,
          3073986821,
          2846688079,
          3818179069,
          2880757123,
          2629329961,
          2948268523,
          2971634249,
          2946830671,
          3130668781,
          2158458187,
          3885987437,
          3353869513,
          4217960377
]

i = 1
totient = 1
for p in primes: 
  i *= p
  totient *= (p-1)
print i
print n
assert i == n


 
d = modinv(e, totient)
s = hex(pow(c, d, n))[2:-1]

print "".join(chr(int(s[i:i+2],16)) for i in xrange(0, len(s), 2))


