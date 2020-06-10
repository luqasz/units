class Prefix:
    __slots__ = ('exp', 'name', 'symbol')

    def __init__(self, name: str, exp: int, symbol: str):
        self.name = name
        self.exp = exp
        self.symbol = symbol

    def __eq__(self, other):
        if not isinstance(other, __class__):
            raise TypeError("{} is not a instance of {}".format(
                other.__class__.__name__,
                __class__.__name__,
            ))
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name, self.exp, self.symbol))

    def __float__(self):
        return float(pow(10, self.exp))

    def __lt__(self, other):
        if not isinstance(other, __class__):
            raise TypeError("{} is not a instance of {}".format(
                other.__class__.__name__,
                __class__.__name__,
            ))
        return self.exp < other.exp

    def __gt__(self, other):
        return not self < other

    def __mul__(self, other):
        return pow(10, self.exp) * other

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return "{} name={self.name} symbol={self.symbol} exponent={self.exp}".format(
            __class__.__name__,
            self=self,
        )


yotta = Prefix(name="yotta", symbol="Y", exp=24)
zetta = Prefix(name="zetta", symbol="Z", exp=21)
exa = Prefix(name="exa", symbol="E", exp=18)
peta = Prefix(name="peta", symbol="P", exp=15)
tera = Prefix(name="tera", symbol="T", exp=12)
giga = Prefix(name="giga", symbol="G", exp=9)
mega = Prefix(name="mega", symbol="M", exp=6)
kilo = Prefix(name="kilo", symbol="k", exp=3)
hecto = Prefix(name="hecto", symbol="h", exp=2)
deca = Prefix(name="deca", symbol="da", exp=1)
deci = Prefix(name="deci", symbol="d", exp=-1)
centi = Prefix(name="centi", symbol="c", exp=-2)
milli = Prefix(name="milli", symbol="m", exp=-3)
micro = Prefix(name="micro", symbol="µ", exp=-6)
nano = Prefix(name="nano", symbol="n", exp=-9)
pico = Prefix(name="pico", symbol="p", exp=-12)
femto = Prefix(name="femto", symbol="f", exp=-15)
atto = Prefix(name="atto", symbol="a", exp=-18)
zepto = Prefix(name="zepto", symbol="z", exp=-21)
yocto = Prefix(name="yocto", symbol="y", exp=-24)

ordered = sorted(
    (
        yocto,
        zepto,
        atto,
        femto,
        pico,
        nano,
        micro,
        milli,
        centi,
        deci,
        deca,
        hecto,
        kilo,
        mega,
        giga,
        tera,
        peta,
        exa,
        zetta,
        yotta,
    )
)

by_exp = dict((prefix.exp, prefix) for prefix in ordered)
by_exp[0] = Prefix(name="none", symbol="", exp=0)
