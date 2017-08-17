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
