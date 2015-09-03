	.file	"a.c"
	.section	.rodata
.LC0:
	.string	"%d"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 5, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 5
	andl	$-16, %rsp
	subl	$32, %rsp
	movq	$5, 20(%rsp)
	movq	$6, 24(%rsp)
	movq	24(%rsp), %eax
	movq	20(%rsp), %edx
	addl	%edx, %eax
	movq	%eax, 216(%rsp)
	movq	216(%rsp), %eax
	movq	%eax, 4(%rsp)
	movq	$.LC0, (%rsp)
	call	printf
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.16.2-19ubuntu1) 4.8.2"
	.section	.note.GNU-stack,"",@progbits
