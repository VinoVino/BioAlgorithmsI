ó
¡Ù[Tc           @   sc   d  Z  d d l m Z d d l Z d   Z d   Z d   Z d   Z e d k r_ e e  n  d S(	   t   jcovinoiÿÿÿÿ(   t   argvNc   
      C   sC  g  } | j  d  d } xO | t |   k  rj |  | } | | } | j  | | t |   | d } q W| t |   } g  } | j  d  d } x¨ | t |   k  r>| d }	 x{ |	 t |   d k  r0| j  | |	 | |  | d k r#|	 t |   k  r#| j  | | |	 | |  n  |	 d }	 q¶ W| d } q W| S(   Ni    i   (   t   appendt   lent   int(
   t   peptidet   massDictt
   preFixMasst   it	   currentAAt   currentMasst   peptideMasst
   cyclicSpect   kt   j(    (    s   CycloPeptideSequencing.pyt   cyclicSpectrum   s*    


 c         C   sª   d d d d d d d d d	 d
 d d d d d d d d g } d } g  } x[ | t  |   k  r¥ x8 | D]0 } t |  |  } | j |  | j |  qd W| d 7} qK W| S(   Ni9   iG   iW   ia   ic   ie   ig   iq   ir   is   i   i   i   i   i   i   i£   iº   i    i   (   R   t   listR   (   t   pListt   aaR   t   newpListt   masst   templist(    (    s   CycloPeptideSequencing.pyt   Expand   s    <c         C   s·   d G|  GHd g g } g  } t  |  } d G| GHd } xz | d k  r² xS | D]K } | |  k r{ | j |  | j |  qL | |  k rL | j |  qL qL Wt  |  | d } q9 W| S(   Ns	   Spectrum i    s   Peptide Listid   i   (   R   R   t   remove(   t   SpectrumR   R   t   FinalR   R   t   Peptide(    (    s   CycloPeptideSequencing.pyt   cycloPeptideSeq-   s     		
c   	      C   s   i  } t  d  } t t | j    } t |  d d  Q } xG | D]? } | j   } | j d  } | d } | d } | | | <qD WWd  QXt | |  GHd  S(   Ns   Enter spectrum: i   t   rt    i    (   t	   raw_inputt   mapR   t   splitt   opent   rstripR   (	   R   R   t   inputR   t	   massTablet   linet   tokenst	   aminoAcidR   (    (    s   CycloPeptideSequencing.pyt   mainA   s    	

t   __main__(	   t
   __author__t   sysR   t	   itertoolsR   R   R   R(   t   __name__(    (    (    s   CycloPeptideSequencing.pyt   <module>   s   				