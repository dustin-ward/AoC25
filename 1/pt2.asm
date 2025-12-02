.global _start
.text
_start:

  movq $0, %r8              ;# ans
  movq $50, %r9             ;# dial
  leaq input, %r10          ;# input_ptr

;# For each line of input
loop:
  cmp $end_input, %r10
  jge print_ans
  movb (%r10), %r11b        ;# first_char
  inc %r10                  ;# input_ptr++
  movq $0, %rax             ;# val

  ;# Read int value after char
loop_int_val:
  movb (%r10), %r13b        ;# *input_ptr
  cmp $0x0A, %r13           ;# '\n'
  je break_loop_int_val
  subq $0x30, %r13          ;# '0'
  imulq $10, %rax           ;# val *= 10
  addq %r13, %rax           ;# val += int(*input_ptr)   
  movq %rax, %r12
  inc %r10                  ;# input_ptr++
  jmp loop_int_val
break_loop_int_val:
  inc %r10                  ;# input_ptr++
  xorq %rdx, %rdx           ;# rdx = 0

  ;# val %= 100
  movq $100, %rcx           ;# d = 100
  divq %rcx                 ;# q, r = val / d
  addq %rax, %r8            ;# ans += q
  movq %rdx, %r12           ;# val = r

  xorq %rdx, %rdx           ;# rdx = 0

  ;# if char == 'L'
  cmp $0x4C, %r11           ;# 'L'
  je turn_left
turn_right:
  cmp $0, %r9               ;# if dial == 0
  je cont_right
  movq $100, %rbx           ;# temp = 100
  subq %r9, %rbx            ;# temp -= dial
  cmp %rbx, %r12            ;# if val < temp
  jl cont_right
  inc %r8                   ;# ans++
cont_right:
  movq %r9, %rax            ;# temp = dial
  addq %r12, %rax           ;# temp += val
  movq $100, %rcx           ;# d = 100
  divq %rcx                 ;# q, r = temp / d
  movq %rdx, %r9            ;# dial = r
  jmp cont_loop
turn_left:
  cmp $0, %r9               ;# if dial == 0
  je cont_left
  cmp %r9, %r12             ;# if val < dial
  jl cont_left
  inc %r8                   ;# ans++
cont_left:
  movq %r9, %rax            ;# temp = dial
  addq $100, %rax           ;# temp += 100
  subq %r12, %rax           ;# temp -= val
  movq $100, %rcx           ;# d = 100
  divq %rcx                 ;# q, r = temp / d
  movq %rdx, %r9            ;# dial = temp

cont_loop:
  jmp loop                  ;# next line
  
print_ans:
  
  ;# to_string()
  leaq end_ans_string, %r10
  dec %r10
  movb $0x0A, (%r10)
  movq %r8, %rax
  movq $10, %rcx
to_str_loop:
  dec %r10
  xorq %rdx, %rdx
  divq %rcx
  addq $0x30, %rdx
  movb %dl, (%r10)
  cmp $0x0, %rax
  jne to_str_loop

  ;# sys_write
  movq $1, %rax
  movq $1, %rdi
  leaq ans_string, %rsi
  movq $8, %rdx
  syscall

  ;# sys_exit
  movq $60, %rax
  xorq %rdi, %rdi
  syscall

.data
ans_string: .ascii "        "
end_ans_string:
input:
        .ascii  "INPUT_GOES_HERE"
end_input:
