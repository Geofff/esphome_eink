#pragma once

#include "esphome/core/component.h"
#include "esphome/components/spi/spi.h"
#include "esphome/components/display/display_buffer.h"
#include "esphome/components/waveshare_epaper/waveshare_epaper.h"


namespace esphome {
    namespace waveshare_epaper {
        class EPaper7P5In_P : public WaveshareEPaper7P5InV2P {
            public:
                void do_full_update();
                void do_partial_update();
        }
    }
}
