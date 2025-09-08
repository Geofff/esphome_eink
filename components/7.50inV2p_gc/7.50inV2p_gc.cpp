#include "7.50inV2p_gc.h"

namespace esphome {
    namespace waveshare_epaper {
       void WaveshareEPaper7P5InV2P_GC::do_full_update() {
        this->at_update_ = 0;
        WaveshareEPaper7P5InV2P::display();
       }
       
       void WaveshareEPaper7P5InV2P_GC::do_partial_update() {
           auto oldUpdate = this->at_update_;
            this->at_update_ = 1;
            WaveshareEPaper7P5InV2P::display();
            this->at_update_ = oldUpdate == 0 ? 0 : (oldUpdate + 1) % this->full_update_every_;
       }
    }
}