/* ==================== GNU C and possibly other UNIX compilers ===================== */
#if !defined(WIN32) || defined(__GNUC__)

    #if defined(__GNUC__) || defined(__linux__)
        #define VOLATILE __volatile__
        #define ASM __asm__
    #else
        /* if we're neither compiling with gcc or under linux, we can hope
         * the following lines work, they probably won't */
        #define ASM asm
        #define VOLATILE
    #endif

    #define TIMESTAMP unsigned long long
    #define INT32 unsigned int

/* ======================== WIN32 ======================= */
#else

    #define TIMESTAMP signed __int64
    #define INT32 unsigned __int32

#endif

/* This is the RDTSC timer.
 * RDTSC is an instruction on several Intel and compatible CPUs that Reads the
 * Time Stamp Counter. The Intel manuals contain more information.
 */


#define COUNTER_LO(a) ((a).int32.lo)
#define COUNTER_HI(a) ((a).int32.hi)
#define COUNTER_VAL(a) ((a).int64)

#define COUNTER(a) \
    ((unsigned long long)COUNTER_VAL(a))

#define COUNTER_DIFF(a,b) \
    (COUNTER(a)-COUNTER(b))

/* ==================== GNU C and possibly other UNIX compilers ===================== */
#if (!defined(WIN32) || defined(__GNUC__)) && defined(__x86_64__)

    typedef union
    {       TIMESTAMP int64;
            struct {INT32 lo, hi;} int32;
    } tsc_counter;

  #define RDTSC(cpu_c) \
      ASM VOLATILE ("rdtsc" : "=a" ((cpu_c).int32.lo), "=d"((cpu_c).int32.hi))
    #define CPUID() \
        ASM VOLATILE ("cpuid" : : "a" (0) : "bx", "cx", "dx" )

/* ======================== WIN32 ======================= */
#elif (!defined(WIN32) || defined(__GNUC__)) && defined(__aarch64__)
    typedef union
    {       TIMESTAMP int64;
            struct {INT32 lo, hi;} int32;
    } tsc_counter;
    #define RDTSC(cpu_c) \
        ASM VOLATILE ("mrs %0, cntvct_el0" : "=r" (cpu_c))
    #define CPUID() ; // no need to do anything for ARM
    // Read the frequency of the CPU
    #define CNTFRQ(cpu_c) \
        ASM VOLATILE ("mrs %0, cntfrq_el0" : "=r" (cpu_c))
#else 

    typedef union
    {       TIMESTAMP int64;
            struct {INT32 lo, hi;} int32;
    } tsc_counter;

    #define RDTSC(cpu_c)   \
    {       __asm rdtsc    \
            __asm mov (cpu_c).int32.lo,eax  \
            __asm mov (cpu_c).int32.hi,edx  \
    }

    #define CPUID() \
    { \
        __asm mov eax, 0 \
        __asm cpuid \
    }

#endif


void init_tsc(void);

TIMESTAMP start_tsc(void);

TIMESTAMP stop_tsc(TIMESTAMP start);
