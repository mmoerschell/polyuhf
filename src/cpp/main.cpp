#define BOOST_TEST_MODULE polyuhf_tests
#include <boost/test/unit_test.hpp>

namespace PolyUHFTesting {

    struct GlobalTestingConfiguration {
        GlobalTestingConfiguration() {
            // 
        }
        ~GlobalTestingConfiguration() {
            //
        }
    };
    BOOST_GLOBAL_FIXTURE(GlobalTestingConfiguration);
}

