.data
a:  .long 0
c:  .long 0
t5: .long 0
t2: .long 0
t3: .long 0
t1: .long 0

.text
.global _start
_start:
movl	3,	%eax
subl	1,	%eax
movl	5,	%edi
movl	%edi,	%ebx
mull	%eax
movl	%eax,	t1
movl	%edi,	%eax
idiv	%ebx
movl	%ebx,	t2
movl	%eax,	t3
mov	    5,  %edx
mov	    t3,  %ecx
mov	    1,  %ebx
mov	    $0x4,  %eax
int	    $0x80
movl	t3,	    %eax
movl	%eax,	%ebx
addl	2,	%ebx
movl	c,	%esi
movl	%esi,	%ebx
addl	6,	%ebx
