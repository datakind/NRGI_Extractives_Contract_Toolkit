## @file rabin_partition.py
## @author Ivan Vlahinic <ivan.newyork@gmail.com>
def rabin_partition(longstr, avgchunk=16, minchunk=8, maxchunk=64, windowsize=16, windowslide=1):
    """
    Optimized python function to partition document into chunks based on Rabin fingerprint. Processing speed 
        is ~300 pages/sec (~1e6 characters/sec) on 2017 Macbook Air. For hepful reference, see: 
        https://moinakg.wordpress.com/2013/06/22/high-performance-content-defined-chunking/
    
    :param longstr: Input document, *str* format
    :param avgchunk: Expected average chunk size acrossthe document
    :param minchunk: Min allowed chunk size (limited to 1/10x *avgchunk*)
    :param maxchunk: Max allowd chunk size (limited to 10x avgchunk)
    :param windowsize: Size of sliding window to be hashed default=16)
    :param windoslide: Sliding interval (default=1)
    :returns: :param longstr broken up into non-overlapping chunks 
    """
    # ensure inputs meet minimum requirements
    from types import StringType
    assert type(longstr) is StringType # *longstr* must be a string
    assert len(longstr) >= windowsize  # *windowsize* must be less than length of *longstr*
    assert windowsize >= windowslide   # *windowsize* should be greater than sliding interval 
    assert windowsize >= minchunk      # *windowsize* should be greater than minimum chunk size
    assert avgchunk%2==0               # *avgchunk* must be a multiple of 2
    
    # limit range of min/max chunksize relative to avg chunk size
    minfactor,maxfactor = 1/10.,10.
    if float(minchunk)/avgchunk < minfactor: minchunk = int(minfactor*avgchunk)
    if float(maxchunk)/avgchunk > maxfactor: maxchunk = int(maxfactor*avgchunk)
    
    # base params
    len_longstr = len(longstr)
    ix_last     = -1
    ix_breaks   = []
    
    # review each sliding window, and based on hash modulo, determine if it is a chunk edge
    for ix in xrange(0, len_longstr - windowsize + windowslide, windowslide):
        # limit min chunk size 
        #   key optimization: ~15% speed-up by skipping review of windows below min chunk size
        if ix < ix_last + minchunk: 
            continue

        # limit max chunk size
        if ix >= ix_last + maxchunk:
            ix_last = ix
            ix_breaks.append(ix)
            continue
        
        # calculate hash of local window and check if it's determine hash
        window = longstr[ix : min(ix+windowsize, len_longstr)]
        if hash(window) % avgchunk == 0:
            ix_breaks.append(ix) 
            ix_last = ix
            
    # export longstr, segmented into chunks, based on Rabin fingerprint
    ix_breaks = [0] + ix_breaks + [len_longstr]
    return [longstr[i:j] for i,j in zip(ix_breaks[:-1],ix_breaks[1:])]

def test_rabin_partition(strlength=3e5,iter=20):
    """
    Generate long random document; test speed of *rabin_partition()*
    Default string length is 3e5 characters, equivalent to ~100 page document
    """
    from tqdm import tqdm
    from random import choice
    from string import ascii_lowercase
    longstr_rand = ''.join([choice(ascii_lowercase) for _ in xrange(int(strlength))])

    print("*rabin_partition* test completed.")
    print("Mac Air baseline is 350 pages/second throughput, i.e. 3.5 iterations per second given a 100 page document")
    for _ in tqdm(xrange(iter)): 
          rabin_partition(longstr_rand)
    return

def example_rabin_partition():
    
    ## document 1
    longstr1 = \
    "Membership of the Union of Soviet Socialist Republics in the United Nations, \
    including the Security Council and all other organs and organizations of the United Nations system, \
    is being continued by the Russian Federation (RSFSR) with the support of the countries of the Commonwealth of \
    Independent States. In this connection, I request that the name 'Russian Federation' should be used in the United \
    Nations in place of the name 'the Union of Soviet Socialist Republics'. The Russian Federation maintains full \
    responsibility for all the rights and obligations of the USSR under the Charter of the United Nations, including \
    the financial obligations. I request that you consider this letter as confirmation of the credentials to represent \
    the Russian Federation in United Nations organs for all the persons currently holding the credentials of representatives \
    of the USSR to the United Nations."

    ## document 2: minor changes inserted into document 1
    longstr2 = \
    "Membership of the Union of Soviet Socialist Republics in the United Nations, \
    including the Security Council and all other organs and organizations of the United Nations system, \
    is being continued by the Russian Federation (RSFSR) with the support of the countries of the Commonwealth of \
    Independent States. In this connection, I request that the name 'Russian Federation' should be used in the United \
    Nations in place of the name 'the ---XXX--- Union of Soviet Socialist Republics'. The Russian Federation maintains full \
    responsibility for all the rights ---|||--- and obligations of the USSR under the Charter of the United Nations, including \
    the financial obligations. I request that you consider this letter as confirmation of the credentials to represent \
    the Russian Federation in United ---ZZZ--- Nations organs for all the persons currently holding the credentials of representatives \
    of the USSR to the United Nations."
    
    minchunk,avgchunk,maxchunk=4,16,32
    a = set(rabin_partition(longstr1,avgchunk,minchunk,maxchunk))
    b = set(rabin_partition(longstr2,avgchunk,minchunk,maxchunk))
    
    print 
    print "EXAMPLE USE CASE: DOCUMENT SIMILARITY"
    print 

    print
    print "Example text 1"
    print longstr1
    print

    print 
    print "Example text 2"
    print  longstr2
    print 

    print 
    print "Percent similarity between document 1 and 2: \n%0.2f%%"%( 100.*len(a&b)/float(min(len(a),len(b))) )

    print 
    print "Common rabin chunks between documents 1 and 2:"
    print [k for k in rabin_partition(longstr1) if k in rabin_partition(longstr2)]

    print 
    print "Non-common rabin chunks between document 1 and 2:"
    print [k for k in rabin_partition(longstr1) if k not in rabin_partition(longstr2)]
    print 
