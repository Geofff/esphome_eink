#include "7P5In_P.h"

namespace esphome {
    namespace waveshare_epaper {
       void EPaper7P5In_P::do_full_update() {
        this->at_update_ = 0;
        WaveshareEPaper7P5InV2P::display();
       }
       
       void EPaper7P5In_P::do_partial_update() {
           auto oldUpdate = this->at_update_;
            this->at_update_ = 1;
            WaveshareEPaper7P5InV2P::display();
            this->at_update_ = oldUpdate == 0 ? 0 : (oldUpdate + 1) % this->full_update_every_;
       }
    }
}